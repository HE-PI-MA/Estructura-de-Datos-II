if __package__:
    from .nodo import Nodo
else:
    from nodo import Nodo


class Arbol:
    def __init__(self):
        self.__raiz = None

    def get_raiz(self):
        return self.__raiz

    def set_raiz(self, nodo):
        self.__raiz = nodo

    def insertar_raiz(self, tablero):
        self.__raiz = Nodo(tablero)
        return self.__raiz

    def agregar_izquierdo(self, nodo_padre, tablero):
        if nodo_padre is None:
            raise ValueError("El nodo padre no puede ser None")

        nuevo_nodo = Nodo(tablero)
        nodo_padre.set_izquierdo(nuevo_nodo)

        return nuevo_nodo

    def agregar_derecho(self, nodo_padre, tablero):
        if nodo_padre is None:
            raise ValueError("El nodo padre no puede ser None")

        nuevo_nodo = Nodo(tablero)
        nodo_padre.set_derecho(nuevo_nodo)

        return nuevo_nodo

    def recorrido_preorden(self, nodo):
        if nodo is not None:
            nodo.mostrar_tablero()

            self.recorrido_preorden(nodo.get_izquierdo())
            self.recorrido_preorden(nodo.get_derecho())

    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.get_izquierdo())

            nodo.mostrar_tablero()

            self.recorrido_inorden(nodo.get_derecho())

    def recorrido_postorden(self, nodo):
        if nodo is not None:
            self.recorrido_postorden(nodo.get_izquierdo())
            self.recorrido_postorden(nodo.get_derecho())

            nodo.mostrar_tablero()

    def buscar_tablero(self, nodo, tablero_buscado):
        if nodo is None:
            return None

        if nodo.get_tablero() == tablero_buscado:
            return nodo

        resultado = self.buscar_tablero(
            nodo.get_izquierdo(),
            tablero_buscado
        )

        if resultado is not None:
            return resultado

        return self.buscar_tablero(
            nodo.get_derecho(),
            tablero_buscado
        )

    def esta_vacio(self):
        return self.__raiz is None