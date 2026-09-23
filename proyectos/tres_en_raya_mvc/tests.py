import unittest
from app import crear_app
from models.juego import jugar, resultado, LINEAS
from models.ia import elegir


class Pruebas(unittest.TestCase):
    def test_lineas_y_empate(self):
        for linea in LINEAS:
            for ficha in ('X', 'O'):
                t = [''] * 9
                for i in linea:
                    t[i] = ficha
                self.assertEqual(resultado(t), ficha)
        self.assertEqual(resultado(list('XOXXOOOXX')), 'empate')

    def test_ia_no_pierde_y_modos_coinciden(self):
        vistos = set()

        def explorar(t):
            if tuple(t) in vistos:
                return
            vistos.add(tuple(t))
            self.assertNotEqual(resultado(t), 'X')
            if resultado(t):
                return
            for i in range(9):
                if t[i]:
                    continue
                nuevo = jugar(t, i, 'X')
                self.assertNotEqual(resultado(nuevo), 'X')
                if resultado(nuevo):
                    continue
                copia = nuevo.copy()
                a, b = elegir(nuevo, False), elegir(nuevo, True)
                self.assertEqual(nuevo, copia)
                self.assertEqual((a['casilla'], a['valor']),
                                 (b['casilla'], b['valor']))
                self.assertLessEqual(b['estados'], a['estados'])
                explorar(jugar(nuevo, b['casilla'], 'O'))

        explorar([''] * 9)
        self.assertGreater(len(vistos), 100)

    def test_rutas_y_sesiones(self):
        app = crear_app()
        app.testing = True
        c = app.test_client()
        self.assertEqual(c.get('/').status_code, 200)
        with c.session_transaction() as s:
            token = s['csrf']
        headers = {'X-CSRF-Token': token}
        self.assertEqual(c.post('/jugar', json={}).status_code, 403)
        for casilla in (-1, 9, True, '0', None):
            self.assertEqual(c.post('/jugar', headers=headers, json={
                'casilla': casilla, 'algoritmo': 'minimax'}).status_code, 400)
        r = c.post('/jugar', headers=headers,
                   json={'casilla': 0, 'algoritmo': 'alfa_beta'})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json['tablero'].count('X'), 1)
        self.assertEqual(r.json['tablero'].count('O'), 1)
        self.assertEqual(c.post('/jugar', headers=headers, json={
            'casilla': 0, 'algoritmo': 'minimax'}).status_code, 400)
        otro = app.test_client()
        otro.get('/')
        with otro.session_transaction() as s:
            self.assertEqual(s['tablero'], [''] * 9)
        self.assertEqual(c.post('/comparar', headers=headers).status_code, 200)
        self.assertEqual(c.post('/reiniciar', headers=headers).json['tablero'],
                         [''] * 9)
        with c.session_transaction() as s:
            s['tablero'] = list('OOOXX X  '.replace(' ', '.'))
        self.assertEqual(c.post('/jugar', headers=headers, json={
            'casilla': 8, 'algoritmo': 'minimax'}).status_code, 400)


if __name__ == '__main__':
    unittest.main()
