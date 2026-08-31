"""Pruebas de la práctica de árboles binarios."""

import unittest

if __package__:
    from .arbol_dinamico import ArbolBinarioDinamico
    from .arbol_estatico import ArbolBinarioEstatico
    from .arbol_expresiones import ArbolExpresiones
else:
    from arbol_dinamico import ArbolBinarioDinamico
    from arbol_estatico import ArbolBinarioEstatico
    from arbol_expresiones import ArbolExpresiones


DATOS = ["A", "B", "C", "D", "E", "F", "G"]
PREORDEN = ["A", "B", "D", "E", "C", "F", "G"]
INORDEN = ["D", "B", "E", "A", "F", "C", "G"]
POSTORDEN = ["D", "E", "B", "F", "G", "C", "A"]


class PruebasArbolEstatico(unittest.TestCase):
    def crear_arbol(self):
        arbol = ArbolBinarioEstatico(capacidad=7)
        for dato in DATOS:
            arbol.InsertarNodo(dato)
        return arbol

    def test_arbol_vacio(self):
        arbol = ArbolBinarioEstatico(capacidad=3)
        self.assertTrue(arbol.EsVacio())
        self.assertEqual(arbol.PreOrden(), [])

    def test_insercion_y_busqueda_existente(self):
        arbol = ArbolBinarioEstatico(capacidad=3)
        self.assertEqual(arbol.InsertarNodo("A"), 0)
        self.assertEqual(arbol.InsertarNodo("B"), 1)
        self.assertFalse(arbol.EsVacio())
        self.assertEqual(arbol.BuscarX("B"), 1)

    def test_busqueda_inexistente(self):
        self.assertIsNone(self.crear_arbol().BuscarX("Z"))

    def test_es_hoja_y_no_es_hoja(self):
        arbol = self.crear_arbol()
        self.assertTrue(arbol.EsHoja(3))
        self.assertFalse(arbol.EsHoja(0))

    def test_recorridos(self):
        arbol = self.crear_arbol()
        self.assertEqual(arbol.InOrden(), INORDEN)
        self.assertEqual(arbol.PreOrden(), PREORDEN)
        self.assertEqual(arbol.PostOrden(), POSTORDEN)

    def test_capacidad_maxima(self):
        arbol = ArbolBinarioEstatico(capacidad=1)
        arbol.InsertarNodo("A")
        with self.assertRaises(OverflowError):
            arbol.InsertarNodo("B")


class PruebasArbolDinamico(unittest.TestCase):
    def crear_arbol(self):
        arbol = ArbolBinarioDinamico()
        for dato in DATOS:
            arbol.InsertarNodo(dato)
        return arbol

    def test_arbol_vacio(self):
        arbol = ArbolBinarioDinamico()
        self.assertTrue(arbol.EsVacio())
        self.assertEqual(arbol.PreOrden(), [])

    def test_insercion_y_busqueda_existente(self):
        arbol = ArbolBinarioDinamico()
        raiz = arbol.InsertarNodo("A")
        arbol.InsertarNodo("B")
        self.assertFalse(arbol.EsVacio())
        self.assertIs(arbol.BuscarX("A"), raiz)
        self.assertEqual(arbol.BuscarX("B").dato, "B")

    def test_busqueda_inexistente(self):
        self.assertIsNone(self.crear_arbol().BuscarX("Z"))

    def test_es_hoja_y_no_es_hoja(self):
        arbol = self.crear_arbol()
        self.assertTrue(arbol.EsHoja(arbol.BuscarX("D")))
        self.assertFalse(arbol.EsHoja(arbol.BuscarX("A")))

    def test_recorridos(self):
        arbol = self.crear_arbol()
        self.assertEqual(arbol.InOrden(), INORDEN)
        self.assertEqual(arbol.PreOrden(), PREORDEN)
        self.assertEqual(arbol.PostOrden(), POSTORDEN)


class PruebasArbolExpresiones(unittest.TestCase):
    def test_conversion_y_construccion(self):
        arbol = ArbolExpresiones()
        arbol.Construir("(A+B)*C")

        self.assertEqual(arbol.ObtenerInfija(), "(A+B)*C")
        self.assertEqual(arbol.ObtenerPosfija(), "AB+C*")
        self.assertEqual(arbol.PreOrden(), ["*", "+", "A", "B", "C"])
        self.assertEqual(arbol.InOrden(), ["A", "+", "B", "*", "C"])
        self.assertEqual(arbol.PostOrden(), ["A", "B", "+", "C", "*"])
        self.assertEqual(arbol.InOrdenConParentesis(), "((A+B)*C)")

    def test_precedencia_y_parentesis(self):
        arbol = ArbolExpresiones()
        self.assertEqual(arbol.InfijaAPosfija("A+B*C"), "ABC*+")
        self.assertEqual(arbol.InfijaAPosfija("A/(B-C)"), "ABC-/")

    def test_expresiones_incorrectas(self):
        incorrectas = ["", "A+", "(A+B", "A++B", "()", "A B", "A$B"]
        arbol = ArbolExpresiones()

        for expresion in incorrectas:
            with self.subTest(expresion=expresion):
                with self.assertRaises(ValueError):
                    arbol.Construir(expresion)


if __name__ == "__main__":
    unittest.main(verbosity=2)
