"""Nodo con hasta m - 1 claves ordenadas y m referencias a hijos."""


class NodoMVias:
    """Almacena claves distintas y reserva None para los hijos vacíos."""

    def __init__(self, orden, claves=None):
        self.validar_orden(orden)
        self.__orden = orden
        self.__claves = []
        self.__hijos = [None] * orden
        if claves is not None:
            self.set_claves(claves)

    @staticmethod
    def validar_orden(orden):
        if isinstance(orden, bool) or not isinstance(orden, int):
            raise TypeError("El orden debe ser un número entero")
        if orden < 2:
            raise ValueError("El orden debe ser al menos 2")

    def get_orden(self):
        return self.__orden

    def set_orden(self, orden):
        """Permite cambiar el orden de un nodo aislado si sus claves caben."""
        self.validar_orden(orden)
        if not self.es_hoja():
            raise ValueError("El nodo tiene hijos; no se puede cambiar el orden")
        if len(self.__claves) >= orden:
            raise ValueError("Las claves no caben en el nuevo orden")
        self.__orden = orden
        self.__hijos = [None] * orden

    def get_claves(self):
        """Devuelve una copia de la lista de claves."""
        return self.__claves.copy()

    def set_claves(self, claves):
        """Asigna claves ordenadas; el árbol verifica los rangos de hijos."""
        nuevas = list(claves)
        if len(nuevas) >= self.__orden:
            raise ValueError("Un nodo admite como máximo orden - 1 claves")
        for clave in nuevas:
            self.validar_clave(clave)
        if any(not a < b for a, b in zip(nuevas, nuevas[1:])):
            raise ValueError("Se requieren claves ordenadas y distintas")
        self.__claves = nuevas

    @staticmethod
    def validar_clave(clave):
        if clave is None:
            raise ValueError("None se reserva para representar ausencia")
        if clave != clave:
            raise ValueError("No se admiten claves NaN")

    def get_clave(self, indice):
        self.__validar_indice(indice, len(self.__claves))
        return self.__claves[indice]

    def set_clave(self, indice, clave):
        self.__validar_indice(indice, len(self.__claves))
        nuevas = self.get_claves()
        nuevas[indice] = clave
        self.set_claves(nuevas)

    def get_hijos(self):
        return self.__hijos.copy()

    def set_hijos(self, hijos):
        nuevos = list(hijos)
        if len(nuevos) > self.__orden:
            raise ValueError("Hay más hijos que los permitidos por el orden")
        for hijo in nuevos:
            self.__validar_hijo(hijo)
        self.__hijos = nuevos + [None] * (self.__orden - len(nuevos))

    def get_hijo(self, indice):
        self.__validar_indice(indice, self.__orden)
        return self.__hijos[indice]

    def set_hijo(self, indice, hijo):
        self.__validar_indice(indice, self.__orden)
        self.__validar_hijo(hijo)
        self.__hijos[indice] = hijo

    def __validar_hijo(self, hijo):
        if hijo is None:
            return
        if not isinstance(hijo, NodoMVias):
            raise TypeError("El hijo debe ser NodoMVias o None")
        if hijo is self:
            raise ValueError("Un nodo no puede ser su propio hijo")
        if hijo.get_orden() != self.__orden:
            raise ValueError("Todos los nodos deben tener el mismo orden")

    @staticmethod
    def __validar_indice(indice, limite):
        if isinstance(indice, bool) or not isinstance(indice, int):
            raise TypeError("El índice debe ser un entero")
        if not 0 <= indice < limite:
            raise IndexError("Índice fuera de rango")

    def cantidad_claves(self):
        return len(self.__claves)

    def es_hoja(self):
        return all(hijo is None for hijo in self.__hijos)

    def esta_lleno(self):
        return len(self.__claves) == self.__orden - 1

    def __repr__(self):
        return f"NodoMVias(claves={self.__claves!r})"
