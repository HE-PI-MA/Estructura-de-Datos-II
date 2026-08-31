"""Definición del nodo usado por el Árbol Binario de Búsqueda."""


class Nodo:
    """Almacena un dato y las referencias a sus hijos."""

    def __init__(self, dato):
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def get_dato(self):
        """Devuelve el dato almacenado en el nodo."""
        return self.__dato

    def set_dato(self, dato):
        """Modifica el dato almacenado en el nodo."""
        self.__dato = dato

    def get_izquierdo(self):
        """Devuelve el hijo izquierdo."""
        return self.__izquierdo

    def set_izquierdo(self, nodo):
        """Asigna un objeto Nodo o None como hijo izquierdo."""
        self.__validar_hijo(nodo)
        self.__izquierdo = nodo

    def get_derecho(self):
        """Devuelve el hijo derecho."""
        return self.__derecho

    def set_derecho(self, nodo):
        """Asigna un objeto Nodo o None como hijo derecho."""
        self.__validar_hijo(nodo)
        self.__derecho = nodo

    @staticmethod
    def __validar_hijo(nodo):
        if nodo is not None and not isinstance(nodo, Nodo):
            raise TypeError("El hijo debe ser un objeto Nodo o None")
