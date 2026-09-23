"""Pruebas de los recorridos y de la conservación del orden al modificar."""

import random
import unittest

if __package__:
    from .arbol_mvias import ArbolMVias
    from .nodo_mvias import NodoMVias
else:
    from arbol_mvias import ArbolMVias
    from nodo_mvias import NodoMVias


def crear(valores, orden=3):
    arbol = ArbolMVias(orden)
    for clave in valores:
        arbol.insertar(clave)
    return arbol


class PruebasNodoMVias(unittest.TestCase):
    def test_getters_setters_y_copias(self):
        nodo = NodoMVias(4, [10, 20])
        hijo = NodoMVias(4, [5])
        nodo.set_clave(1, 25)
        nodo.set_hijo(0, hijo)
        nodo.get_claves().clear()
        nodo.get_hijos().clear()
        self.assertEqual(nodo.get_claves(), [10, 25])
        self.assertIs(nodo.get_hijo(0), hijo)
        self.assertFalse(nodo.es_hoja())
        nodo.set_hijos([])
        nodo.set_orden(3)
        self.assertEqual(nodo.get_orden(), 3)
        self.assertTrue(nodo.es_hoja())
        self.assertTrue(nodo.esta_lleno())

    def test_rechaza_capacidad_orden_indices_y_claves_invalidas(self):
        nodo = NodoMVias(3, [10, 20])
        for claves in ([10, 10], [20, 10], [1, 2, 3], [None]):
            with self.assertRaises(ValueError):
                nodo.set_claves(claves)
        with self.assertRaises(ValueError):
            nodo.set_hijo(0, NodoMVias(4))
        with self.assertRaises(ValueError):
            nodo.set_hijo(0, nodo)
        with self.assertRaises(TypeError):
            nodo.set_hijo(0, 20)
        for indice in (-1, 3):
            with self.assertRaises(IndexError):
                nodo.get_hijo(indice)
        self.assertEqual(nodo.get_claves(), [10, 20])


class PruebasArbolMVias(unittest.TestCase):
    def test_arbol_vacio(self):
        arbol = ArbolMVias()
        self.assertTrue(arbol.EstaVacio())
        self.assertEqual(arbol.Raiz(), [])
        self.assertEqual(arbol.Altura(), -1)
        self.assertEqual(arbol.Cantidad(), 0)
        self.assertEqual(arbol.CantidadClaves(), 0)
        self.assertEqual(arbol.CantidadHojas(), 0)
        self.assertEqual(arbol.Amplitud(), 0)
        self.assertEqual(arbol.InOrden(), [])
        self.assertEqual(arbol.PreOrden(), [])
        self.assertEqual(arbol.PostOrden(), [])
        self.assertEqual(arbol.PorNiveles(), [])
        self.assertIsNone(arbol.Minimo())
        self.assertIsNone(arbol.Maximo())
        self.assertFalse(arbol.Eliminar(5))
        self.assertIsNone(arbol.Buscar(5))
        self.assertTrue(arbol.EsBalanceado())

    def test_recorridos_y_metricas_con_varias_claves_por_nodo(self):
        arbol = crear([30, 50, 10, 20, 40, 60, 70])
        self.assertEqual(arbol.InOrden(), [10, 20, 30, 40, 50, 60, 70])
        self.assertEqual(arbol.PreOrden(), [30, 10, 20, 50, 40, 60, 70])
        self.assertEqual(arbol.PostOrden(), [10, 20, 40, 30, 60, 70, 50])
        self.assertEqual(
            arbol.PorNiveles(), [[30, 50], [10, 20], [40], [60, 70]]
        )
        self.assertEqual(
            arbol.niveles(), [[[30, 50]], [[10, 20], [40], [60, 70]]]
        )
        self.assertEqual(arbol.Cantidad(), 4)
        self.assertEqual(arbol.CantidadClaves(), 7)
        self.assertEqual(len(arbol), 7)
        self.assertEqual(arbol.CantidadHojas(), 3)
        self.assertEqual(arbol.Amplitud(), 3)
        self.assertEqual(arbol.Altura(), 1)
        self.assertEqual((arbol.Minimo(), arbol.Maximo()), (10, 70))
        self.assertTrue(arbol.EsHoja(arbol.Buscar(20)))
        self.assertFalse(arbol.EsHoja(arbol.Buscar(30)))
        self.assertFalse(arbol.EsHoja(None))

    def test_orden_dos_conserva_recorridos_del_abb(self):
        arbol = crear([50, 30, 70, 20, 40, 60, 80], 2)
        self.assertEqual(arbol.PreOrden(), [50, 30, 20, 40, 70, 60, 80])
        self.assertEqual(arbol.PostOrden(), [20, 40, 30, 60, 80, 70, 50])
        self.assertEqual(arbol.Cantidad(), 7)
        self.assertEqual(arbol.Altura(), 2)
        self.assertEqual(arbol.Amplitud(), 4)

    def test_busqueda_y_duplicados(self):
        arbol = crear([30, 50, 10, 20, 40])
        antes = arbol.PorNiveles()
        for clave in [30, 50, 10, 20, 40]:
            self.assertFalse(arbol.Insertar(clave))
            self.assertTrue(arbol.buscar(clave))
            self.assertIn(clave, arbol.Buscar(clave).get_claves())
        self.assertEqual(arbol.PorNiveles(), antes)
        self.assertFalse(arbol.buscar(99))

    def test_eliminar_hoja_hasta_vaciar_y_reinsertar(self):
        arbol = crear([10, 20])
        self.assertTrue(arbol.Eliminar(10))
        self.assertEqual(arbol.Raiz(), [20])
        self.assertTrue(arbol.Eliminar(20))
        self.assertTrue(arbol.EstaVacio())
        self.assertEqual(arbol.Altura(), -1)
        self.assertTrue(arbol.Insertar(9))
        self.assertEqual(arbol.Raiz(), [9])

    def test_eliminar_clave_interna_con_sucesor(self):
        arbol = crear([30, 50, 10, 40, 60])
        self.assertTrue(arbol.Eliminar(30))
        self.assertEqual(arbol.Raiz(), [40, 50])
        self.assertEqual(arbol.InOrden(), [10, 40, 50, 60])
        self.assertTrue(arbol.validar())

    def test_eliminar_con_predecesor_si_no_hay_hijo_derecho(self):
        arbol = crear([30, 50, 10, 20])
        self.assertTrue(arbol.Eliminar(30))
        self.assertEqual(arbol.Raiz(), [20, 50])
        self.assertEqual(arbol.InOrden(), [10, 20, 50])
        self.assertTrue(arbol.validar())

    def test_eliminar_clave_entre_hijos_vacios_y_reinsertar(self):
        arbol = crear([20, 40, 60, 10, 70], 4)
        self.assertTrue(arbol.Eliminar(40))
        self.assertEqual(arbol.PorNiveles(), [[20, 60], [10], [70]])
        arbol.Insertar(50)
        self.assertEqual(arbol.PorNiveles(), [[20, 60], [10], [50], [70]])
        self.assertEqual(arbol.InOrden(), [10, 20, 50, 60, 70])
        self.assertTrue(arbol.validar())

    def test_eliminar_inexistente_no_modifica(self):
        arbol = crear([30, 50, 10, 40, 60])
        antes = arbol.PorNiveles()
        self.assertFalse(arbol.Eliminar(99))
        self.assertEqual(arbol.PorNiveles(), antes)

    def test_operaciones_mezcladas_contra_un_conjunto(self):
        for orden in [2, 3, 4, 6]:
            with self.subTest(orden=orden):
                rng = random.Random(orden)
                arbol = ArbolMVias(orden)
                esperado = set()
                for _ in range(250):
                    clave = rng.randrange(80)
                    if rng.random() < 0.6:
                        self.assertEqual(
                            arbol.Insertar(clave), clave not in esperado
                        )
                        esperado.add(clave)
                    else:
                        self.assertEqual(
                            arbol.Eliminar(clave), clave in esperado
                        )
                        esperado.discard(clave)
                    self.assertEqual(arbol.InOrden(), sorted(esperado))
                    self.assertEqual(len(arbol), len(esperado))
                    self.assertTrue(arbol.validar())
                    self.assertEqual(
                        arbol.Minimo(), min(esperado, default=None)
                    )
                    self.assertEqual(
                        arbol.Maximo(), max(esperado, default=None)
                    )
                restantes = list(esperado)
                rng.shuffle(restantes)
                for clave in restantes:
                    self.assertTrue(arbol.Eliminar(clave))
                    esperado.remove(clave)
                    self.assertEqual(arbol.InOrden(), sorted(esperado))
                    self.assertTrue(arbol.validar())
                self.assertTrue(arbol.EstaVacio())

    def test_raiz_valida_y_rechazo_sin_perder_arbol(self):
        arbol = crear([30], 3)
        raiz = NodoMVias(3, [20, 40])
        raiz.set_hijo(1, NodoMVias(3, [30]))
        arbol.set_raiz(raiz)
        self.assertEqual(arbol.InOrden(), [20, 30, 40])
        invalida = NodoMVias(3, [20])
        invalida.set_hijo(0, NodoMVias(3, [50]))
        with self.assertRaises(ValueError):
            arbol.set_raiz(invalida)
        self.assertIs(arbol.get_raiz(), raiz)
        with self.assertRaises(ValueError):
            arbol.set_raiz(NodoMVias(4, [1]))
        with self.assertRaises(ValueError):
            arbol.set_raiz(NodoMVias(3))
        arbol.set_raiz(None)
        self.assertTrue(arbol.EstaVacio())

    def test_rechaza_ciclos_y_referencias_compartidas(self):
        a = NodoMVias(3, [20])
        b = NodoMVias(3, [10])
        a.set_hijo(0, b)
        b.set_hijo(1, a)
        with self.assertRaises(ValueError):
            ArbolMVias(3).set_raiz(a)
        b.set_hijo(1, None)
        a.set_hijo(1, b)
        with self.assertRaises(ValueError):
            ArbolMVias(3).set_raiz(a)

    def test_balance_y_orden_configurable(self):
        arbol = crear([10, 20, 30, 40], 2)
        self.assertFalse(arbol.EsBalanceado())
        with self.assertRaises(ValueError):
            arbol.set_orden(4)
        arbol.vaciar()
        arbol.set_orden(4)
        self.assertEqual(arbol.get_orden(), 4)
        self.assertTrue(arbol.EsBalanceado())
        for orden in (0, 1, -1):
            with self.assertRaises(ValueError):
                ArbolMVias(orden)
        for orden in (True, 3.5, "4"):
            with self.assertRaises(TypeError):
                ArbolMVias(orden)

    def test_claves_texto_y_errores_de_tipo(self):
        arbol = crear(["perro", "gato", "ave", "pez"])
        self.assertEqual(arbol.InOrden(), ["ave", "gato", "perro", "pez"])
        self.assertTrue(arbol.Eliminar("gato"))
        self.assertTrue(arbol.validar())
        for clave in [None, float("nan")]:
            with self.assertRaises(ValueError):
                arbol.Insertar(clave)
        with self.assertRaises(TypeError):
            arbol.Insertar(5)
        self.assertEqual(arbol.InOrden(), ["ave", "perro", "pez"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
