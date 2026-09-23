"""Pruebas automáticas del Árbol Binario de Búsqueda."""

import unittest

if __package__:
    from .arbol_binario_busqueda import ArbolBinarioBusqueda
    from .nodo import Nodo
else:
    from arbol_binario_busqueda import ArbolBinarioBusqueda
    from nodo import Nodo


VALORES = [50, 30, 70, 20, 40, 60, 80]


class PruebasNodo(unittest.TestCase):
    """Comprueba el encapsulamiento y los métodos de Nodo."""

    def test_getters_y_setters(self):
        nodo = Nodo(10)
        izquierdo = Nodo(5)
        derecho = Nodo(15)

        self.assertEqual(nodo.get_dato(), 10)
        self.assertIsNone(nodo.get_izquierdo())
        self.assertIsNone(nodo.get_derecho())

        nodo.set_dato(11)
        nodo.set_izquierdo(izquierdo)
        nodo.set_derecho(derecho)

        self.assertEqual(nodo.get_dato(), 11)
        self.assertIs(nodo.get_izquierdo(), izquierdo)
        self.assertIs(nodo.get_derecho(), derecho)

        nodo.set_izquierdo(None)
        nodo.set_derecho(None)
        self.assertIsNone(nodo.get_izquierdo())
        self.assertIsNone(nodo.get_derecho())

    def test_setters_rechazan_hijos_invalidos(self):
        nodo = Nodo(10)

        with self.assertRaises(TypeError):
            nodo.set_izquierdo(5)
        with self.assertRaises(TypeError):
            nodo.set_derecho("15")


class PruebasArbolBinarioBusqueda(unittest.TestCase):
    """Comprueba todas las operaciones solicitadas para el ABB."""

    def crear_arbol(self):
        arbol = ArbolBinarioBusqueda()
        for valor in VALORES:
            arbol.Insertar(valor)
        return arbol

    def test_arbol_inicialmente_vacio(self):
        arbol = ArbolBinarioBusqueda()

        self.assertIsNone(arbol.get_raiz())
        self.assertEqual(arbol.Cantidad(), 0)
        self.assertEqual(arbol.Amplitud(), 0)
        self.assertEqual(arbol.InOrden(), [])

    def test_insertar_raiz(self):
        arbol = ArbolBinarioBusqueda()

        self.assertTrue(arbol.Insertar(50))
        self.assertEqual(arbol.get_raiz().get_dato(), 50)

    def test_insertar_varios_valores(self):
        arbol = self.crear_arbol()
        raiz = arbol.get_raiz()

        self.assertEqual(raiz.get_dato(), 50)
        self.assertEqual(raiz.get_izquierdo().get_dato(), 30)
        self.assertEqual(raiz.get_derecho().get_dato(), 70)
        self.assertEqual(
            raiz.get_izquierdo().get_izquierdo().get_dato(),
            20,
        )
        self.assertEqual(
            raiz.get_derecho().get_derecho().get_dato(),
            80,
        )

    def test_duplicados(self):
        arbol = self.crear_arbol()

        self.assertFalse(arbol.Insertar(40))
        self.assertEqual(arbol.Cantidad(), 7)

    def test_buscar_valor_existente(self):
        nodo = self.crear_arbol().Buscar(60)

        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.get_dato(), 60)

    def test_buscar_valor_inexistente(self):
        self.assertIsNone(self.crear_arbol().Buscar(99))

    def test_es_hoja_verdadero(self):
        arbol = self.crear_arbol()

        self.assertTrue(arbol.EsHoja(arbol.Buscar(20)))

    def test_es_hoja_falso(self):
        arbol = self.crear_arbol()

        self.assertFalse(arbol.EsHoja(arbol.Buscar(30)))

    def test_altura_arbol_vacio(self):
        self.assertEqual(ArbolBinarioBusqueda().Altura(), -1)

    def test_altura_un_solo_nodo(self):
        arbol = ArbolBinarioBusqueda()
        arbol.Insertar(50)

        self.assertEqual(arbol.Altura(), 0)

    def test_altura_varios_niveles(self):
        self.assertEqual(self.crear_arbol().Altura(), 2)

    def test_cantidad(self):
        self.assertEqual(self.crear_arbol().Cantidad(), 7)

    def test_amplitud(self):
        self.assertEqual(self.crear_arbol().Amplitud(), 4)

    def test_inorden(self):
        esperado = [20, 30, 40, 50, 60, 70, 80]

        self.assertEqual(self.crear_arbol().InOrden(), esperado)

    def test_preorden(self):
        esperado = [50, 30, 20, 40, 70, 60, 80]

        self.assertEqual(self.crear_arbol().PreOrden(), esperado)

    def test_postorden(self):
        esperado = [20, 40, 30, 60, 80, 70, 50]

        self.assertEqual(self.crear_arbol().PostOrden(), esperado)

    def test_getter_y_setter_raiz(self):
        arbol = ArbolBinarioBusqueda()
        raiz = Nodo(25)

        arbol.set_raiz(raiz)
        self.assertIs(arbol.get_raiz(), raiz)

        arbol.set_raiz(None)
        self.assertIsNone(arbol.get_raiz())

    def test_setter_raiz_rechaza_tipo_invalido(self):
        arbol = ArbolBinarioBusqueda()

        with self.assertRaises(TypeError):
            arbol.set_raiz(50)


if __name__ == "__main__":
    unittest.main(verbosity=2)
