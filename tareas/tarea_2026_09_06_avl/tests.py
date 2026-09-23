import unittest

if __package__:
    from .arbol_avl import ArbolAVL
else:
    from arbol_avl import ArbolAVL


class PruebasAVL(unittest.TestCase):

    def test_arbol_vacio(self):
        arbol = ArbolAVL()
        self.assertIsNone(arbol.get_raiz())

    def test_insertar_y_buscar(self):
        arbol = ArbolAVL()

        for valor in [50, 30, 70, 20, 40]:
            arbol.insertar(valor)

        self.assertIsNotNone(arbol.buscar(40))
        self.assertIsNone(arbol.buscar(100))

    def test_inorden(self):
        arbol = ArbolAVL()

        for valor in [50, 30, 70, 20, 40]:
            arbol.insertar(valor)

        self.assertEqual(
            arbol.inorden(),
            [20, 30, 40, 50, 70]
        )

    def test_rotacion_ll(self):
        arbol = ArbolAVL()

        for valor in [30, 20, 10]:
            arbol.insertar(valor)

        self.assertEqual(
            arbol.preorden(),
            [20, 10, 30]
        )

    def test_rotacion_rr(self):
        arbol = ArbolAVL()

        for valor in [10, 20, 30]:
            arbol.insertar(valor)

        self.assertEqual(
            arbol.preorden(),
            [20, 10, 30]
        )

    def test_rotacion_lr(self):
        arbol = ArbolAVL()

        for valor in [30, 10, 20]:
            arbol.insertar(valor)

        self.assertEqual(
            arbol.preorden(),
            [20, 10, 30]
        )

    def test_rotacion_rl(self):
        arbol = ArbolAVL()

        for valor in [10, 30, 20]:
            arbol.insertar(valor)

        self.assertEqual(
            arbol.preorden(),
            [20, 10, 30]
        )

    def test_cantidad(self):
        arbol = ArbolAVL()

        for valor in [50, 30, 70]:
            arbol.insertar(valor)

        self.assertEqual(
            arbol.cantidad(),
            3
        )

    def test_eliminar(self):
        arbol = ArbolAVL()

        for valor in [50, 30, 70, 20, 40]:
            arbol.insertar(valor)

        arbol.eliminar(30)

        self.assertIsNone(
            arbol.buscar(30)
        )


if __name__ == "__main__":
    unittest.main()
