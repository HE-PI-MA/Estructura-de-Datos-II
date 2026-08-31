"""Árbol binario dinámico construido mediante nodos enlazados."""

from collections import deque


class Nodo:
    """Nodo con un dato y referencias a sus dos posibles hijos."""

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioDinamico:
    """Árbol binario general con inserción por nivel."""

    def __init__(self):
        self.raiz = None

    def InsertarNodo(self, x):
        """Inserta ``x`` de izquierda a derecha y devuelve el nuevo nodo."""
        if x is None:
            raise ValueError("El dato del nodo no puede ser None")

        nuevo = Nodo(x)
        if self.raiz is None:
            self.raiz = nuevo
            return nuevo

        pendientes = deque([self.raiz])
        while pendientes:
            actual = pendientes.popleft()

            if actual.izquierdo is None:
                actual.izquierdo = nuevo
                return nuevo
            pendientes.append(actual.izquierdo)

            if actual.derecho is None:
                actual.derecho = nuevo
                return nuevo
            pendientes.append(actual.derecho)

    def EsVacio(self):
        """Indica si el árbol no contiene nodos."""
        return self.raiz is None

    def EsHoja(self, nodo=None):
        """Indica si ``nodo`` no tiene hijos; sin argumento revisa la raíz."""
        if nodo is None:
            nodo = self.raiz
        return (
            nodo is not None
            and nodo.izquierdo is None
            and nodo.derecho is None
        )

    def BuscarX(self, x):
        """Devuelve el primer nodo cuyo dato sea ``x`` o ``None``."""
        if self.raiz is None:
            return None

        pendientes = deque([self.raiz])
        while pendientes:
            actual = pendientes.popleft()
            if actual.dato == x:
                return actual

            if actual.izquierdo is not None:
                pendientes.append(actual.izquierdo)
            if actual.derecho is not None:
                pendientes.append(actual.derecho)

        return None

    def InOrden(self):
        """Devuelve los datos en el orden izquierdo, raíz, derecho."""
        recorrido = []
        self.__inorden(self.raiz, recorrido)
        return recorrido

    def PostOrden(self):
        """Devuelve los datos en el orden izquierdo, derecho, raíz."""
        recorrido = []
        self.__postorden(self.raiz, recorrido)
        return recorrido

    def PreOrden(self):
        """Devuelve los datos en el orden raíz, izquierdo, derecho."""
        recorrido = []
        self.__preorden(self.raiz, recorrido)
        return recorrido

    def __inorden(self, nodo, recorrido):
        if nodo is None:
            return
        self.__inorden(nodo.izquierdo, recorrido)
        recorrido.append(nodo.dato)
        self.__inorden(nodo.derecho, recorrido)

    def __postorden(self, nodo, recorrido):
        if nodo is None:
            return
        self.__postorden(nodo.izquierdo, recorrido)
        self.__postorden(nodo.derecho, recorrido)
        recorrido.append(nodo.dato)

    def __preorden(self, nodo, recorrido):
        if nodo is None:
            return
        recorrido.append(nodo.dato)
        self.__preorden(nodo.izquierdo, recorrido)
        self.__preorden(nodo.derecho, recorrido)
