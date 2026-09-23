"""Pruebas de las operaciones web y sus invariantes."""
import unittest

if __package__:
    from .app import create_app
else:
    from app import create_app


class InterfazTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app({'TESTING': True, 'SECRET_KEY': 'pruebas'})
        self.cliente = self.app.test_client()
        self.token = self.estado()['csrf']

    def estado(self):
        return self.cliente.get('/api/arbol').get_json()

    def enviar(self, accion, **datos):
        return self.cliente.post('/api/operar', json={'accion': accion, **datos},
                                 headers={'X-CSRF-Token': self.token})

    def operar(self, accion, **datos):
        respuesta = self.enviar(accion, **datos)
        self.assertEqual(respuesta.status_code, 200, respuesta.get_json())
        return respuesta.get_json()

    def test_pagina_y_estaticos(self):
        for ruta in ('/', '/static/arbol.js', '/static/estilos.css', '/static/arbol.svg'):
            respuesta = self.cliente.get(ruta)
            self.assertEqual(respuesta.status_code, 200)
            respuesta.close()

    def test_vacio(self):
        self.assertEqual(self.estado()['resumen']['altura'], -1)
        for accion in ('minimo', 'maximo', 'raiz'):
            self.assertIsNone(self.operar(accion)['destacado'])

    def test_recorridos_y_medidas(self):
        estado = self.operar('ejemplo')
        self.assertEqual(estado['recorridos'], {
            'inorden': [20, 30, 40, 50, 60, 70, 80],
            'preorden': [50, 30, 20, 40, 70, 60, 80],
            'postorden': [20, 40, 30, 60, 80, 70, 50],
            'niveles': [50, 30, 70, 20, 40, 60, 80],
        })
        self.assertEqual(estado['resumen'], {
            'cantidad': 7, 'altura': 2, 'hojas': 4, 'amplitud': 4,
            'raiz': 50, 'minimo': 20, 'maximo': 80,
            'vacio': False, 'balanceado': True,
        })

    def test_busqueda_y_hojas(self):
        self.operar('ejemplo')
        self.assertEqual(self.operar('buscar', valor=40)['camino'], [50, 30, 40])
        self.assertFalse(self.operar('buscar', valor=35)['encontrado'])
        self.assertIn('es una hoja:', self.operar('es_hoja', valor=20)['mensaje'])
        self.assertIn('no es una hoja:', self.operar('es_hoja', valor=30)['mensaje'])

    def test_consultas(self):
        self.operar('ejemplo')
        for accion, valor in (('raiz', 50), ('minimo', 20), ('maximo', 80)):
            self.assertEqual(self.operar(accion)['destacado'], valor)

    def test_duplicados_negativos_cero(self):
        estado = self.operar('insertar', valores='0, -5; 5 0 -5')
        self.assertEqual(estado['recorridos']['inorden'], [-5, 0, 5])
        self.assertIn('2 duplicados', estado['mensaje'])

    def test_eliminar_tres_casos_y_conservar_forma(self):
        self.operar('ejemplo')
        self.operar('eliminar', valor=20)  # Hoja.
        self.operar('eliminar', valor=30)  # Un hijo.
        estado = self.operar('eliminar', valor=50)  # Raíz con dos hijos.
        self.assertEqual(estado['recorridos']['preorden'], [60, 40, 70, 80])
        self.assertEqual(estado['recorridos']['inorden'], [40, 60, 70, 80])
        self.assertEqual(self.estado()['recorridos'], estado['recorridos'])

    def test_eliminar_ultimo_y_ausente(self):
        self.operar('insertar', valores='10')
        self.assertFalse(self.operar('eliminar', valor=99)['encontrado'])
        self.assertTrue(self.operar('eliminar', valor=10)['resumen']['vacio'])

    def test_grafico_respeta_hijos(self):
        estado = self.operar('ejemplo')
        grafico = estado['grafico']
        nodos = {n['valor']: n for n in grafico['nodos']}
        self.assertEqual(len(grafico['enlaces']), 6)
        for enlace in grafico['enlaces']:
            padre, hijo = nodos[enlace['desde']], nodos[enlace['hasta']]
            self.assertGreater(hijo['y'], padre['y'])
            if enlace['lado'] == 'I':
                self.assertLess(hijo['x'], padre['x'])
            else:
                self.assertGreater(hijo['x'], padre['x'])

    def test_arbol_inclinado(self):
        resumen = self.operar('insertar', valores='10 20 30 40')['resumen']
        self.assertFalse(resumen['balanceado'])
        self.assertEqual(resumen['altura'], 3)
        self.assertEqual(resumen['amplitud'], 1)

    def test_recarga_y_sesiones_independientes(self):
        original = self.operar('insertar', valores='30 10 20 50 40')
        self.assertEqual(self.estado()['recorridos'], original['recorridos'])
        otro = self.app.test_client().get('/api/arbol').get_json()
        self.assertEqual(otro['resumen']['cantidad'], 0)

    def test_lote_invalido_no_inserta_parcialmente(self):
        self.operar('insertar', valores='50')
        for valores in ('20 error 30', '2.5', '10000', '', None, [1, 2]):
            self.assertEqual(self.enviar('insertar', valores=valores).status_code, 400)
            self.assertEqual(self.estado()['recorridos']['inorden'], [50])

    def test_limite_de_nodos(self):
        self.operar('insertar', valores=' '.join(map(str, range(63))))
        self.assertEqual(self.enviar('insertar', valores='90').status_code, 400)
        self.assertEqual(self.estado()['resumen']['cantidad'], 63)
        self.assertEqual(self.operar('insertar', valores='5')['resumen']['cantidad'], 63)

    def test_tipo_y_rango(self):
        for valor in (True, 1.2, '20', None, -10000, 10000):
            self.assertEqual(self.enviar('buscar', valor=valor).status_code, 400)

    def test_solicitudes_invalidas(self):
        self.operar('ejemplo')
        self.assertEqual(self.enviar('desconocida').status_code, 400)
        respuesta = self.cliente.post('/api/operar', json={'accion': 'vaciar'})
        self.assertEqual(respuesta.status_code, 403)
        respuesta = self.cliente.post('/api/operar', json=[], headers={'X-CSRF-Token': self.token})
        self.assertEqual(respuesta.status_code, 400)
        self.assertEqual(self.estado()['resumen']['cantidad'], 7)

    def test_vaciar(self):
        self.operar('ejemplo')
        self.operar('vaciar')
        self.assertEqual(self.estado()['recorridos']['niveles'], [])


if __name__ == '__main__':
    unittest.main()
