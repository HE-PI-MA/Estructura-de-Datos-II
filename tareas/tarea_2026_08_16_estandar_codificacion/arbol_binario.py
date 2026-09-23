"""Define la estructura de un árbol binario y el acceso a su raíz."""

if __package__:
    from .nodo import Nodo
else:
    from nodo import Nodo


class ArbolBinario:
    """Representa un árbol binario mediante su nodo raíz."""

    def __init__(self, raiz=None):
        """Crea un árbol vacío o con la raíz recibida."""
        self.__raiz = None
        self.set_raiz(raiz)

    def get_raiz(self):
        """Devuelve la raíz o None cuando el árbol está vacío."""
        return self.__raiz

    def set_raiz(self, nodo):
        """Asigna un Nodo como raíz o vacía el árbol con None."""
        if nodo is not None and not isinstance(nodo, Nodo):
            raise TypeError("La raíz debe ser Nodo o None.")
        self.__raiz = nodo
