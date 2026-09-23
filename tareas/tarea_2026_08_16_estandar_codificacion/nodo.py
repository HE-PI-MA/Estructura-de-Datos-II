"""Define un nodo con un dato y hasta dos hijos."""


class Nodo:
    """Guarda un dato y las referencias a sus hijos."""

    def __init__(self, dato=None):
        """Crea un nodo sin hijos con el dato recibido."""
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def get_dato(self):
        """Devuelve el dato del nodo."""
        return self.__dato

    def set_dato(self, dato):
        """Actualiza el dato del nodo."""
        self.__dato = dato

    def get_izquierdo(self):
        """Devuelve el hijo izquierdo o None si no existe."""
        return self.__izquierdo

    def set_izquierdo(self, nodo):
        """Asigna un Nodo como hijo izquierdo o lo retira con None."""
        if nodo is not None and not isinstance(nodo, Nodo):
            raise TypeError("El hijo izquierdo debe ser Nodo o None.")
        self.__izquierdo = nodo

    def get_derecho(self):
        """Devuelve el hijo derecho o None si no existe."""
        return self.__derecho

    def set_derecho(self, nodo):
        """Asigna un Nodo como hijo derecho o lo retira con None."""
        if nodo is not None and not isinstance(nodo, Nodo):
            raise TypeError("El hijo derecho debe ser Nodo o None.")
        self.__derecho = nodo
