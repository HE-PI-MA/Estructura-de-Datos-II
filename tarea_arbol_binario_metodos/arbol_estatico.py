"""Árbol binario almacenado en un arreglo de capacidad fija."""


class ArbolBinarioEstatico:
    """Representa un árbol binario general mediante una lista de tamaño fijo.

    Los nodos se insertan por nivel, de izquierda a derecha. Para un nodo que
    ocupa la posición ``i``, sus hijos se encuentran en ``2*i + 1`` y
    ``2*i + 2``.
    """

    def __init__(self, capacidad=15):
        if isinstance(capacidad, bool) or not isinstance(capacidad, int):
            raise TypeError("La capacidad debe ser un número entero")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero")

        self.__capacidad = capacidad
        self.__nodos = [None] * capacidad

    @property
    def capacidad(self):
        """Devuelve la capacidad máxima del árbol."""
        return self.__capacidad

    @property
    def nodos(self):
        """Devuelve una copia del arreglo usado para representar el árbol."""
        return self.__nodos.copy()

    def InsertarNodo(self, x):
        """Inserta ``x`` en el primer espacio disponible y devuelve su índice."""
        if x is None:
            raise ValueError("None se reserva para representar una posición vacía")

        for indice, dato in enumerate(self.__nodos):
            if dato is None:
                self.__nodos[indice] = x
                return indice

        raise OverflowError("El árbol alcanzó su capacidad máxima")

    def EsVacio(self):
        """Indica si el árbol no contiene nodos."""
        return self.__nodos[0] is None

    def EsHoja(self, indice=0):
        """Indica si el nodo de ``indice`` existe y no tiene hijos.

        Si no se proporciona un índice, se comprueba la raíz.
        """
        self.__validar_indice(indice)

        if self.__nodos[indice] is None:
            return False

        izquierdo = 2 * indice + 1
        derecho = 2 * indice + 2
        tiene_izquierdo = (
            izquierdo < self.__capacidad
            and self.__nodos[izquierdo] is not None
        )
        tiene_derecho = (
            derecho < self.__capacidad
            and self.__nodos[derecho] is not None
        )
        return not tiene_izquierdo and not tiene_derecho

    def BuscarX(self, x):
        """Devuelve el índice de la primera aparición de ``x`` o ``None``."""
        for indice, dato in enumerate(self.__nodos):
            if dato is not None and dato == x:
                return indice
        return None

    def InOrden(self):
        """Devuelve los datos en el orden izquierdo, raíz, derecho."""
        recorrido = []
        self.__inorden(0, recorrido)
        return recorrido

    def PostOrden(self):
        """Devuelve los datos en el orden izquierdo, derecho, raíz."""
        recorrido = []
        self.__postorden(0, recorrido)
        return recorrido

    def PreOrden(self):
        """Devuelve los datos en el orden raíz, izquierdo, derecho."""
        recorrido = []
        self.__preorden(0, recorrido)
        return recorrido

    def __validar_indice(self, indice):
        if isinstance(indice, bool) or not isinstance(indice, int):
            raise TypeError("El índice debe ser un número entero")
        if indice < 0 or indice >= self.__capacidad:
            raise IndexError("El índice está fuera de la capacidad del árbol")

    def __inorden(self, indice, recorrido):
        if indice >= self.__capacidad or self.__nodos[indice] is None:
            return

        self.__inorden(2 * indice + 1, recorrido)
        recorrido.append(self.__nodos[indice])
        self.__inorden(2 * indice + 2, recorrido)

    def __postorden(self, indice, recorrido):
        if indice >= self.__capacidad or self.__nodos[indice] is None:
            return

        self.__postorden(2 * indice + 1, recorrido)
        self.__postorden(2 * indice + 2, recorrido)
        recorrido.append(self.__nodos[indice])

    def __preorden(self, indice, recorrido):
        if indice >= self.__capacidad or self.__nodos[indice] is None:
            return

        recorrido.append(self.__nodos[indice])
        self.__preorden(2 * indice + 1, recorrido)
        self.__preorden(2 * indice + 2, recorrido)
