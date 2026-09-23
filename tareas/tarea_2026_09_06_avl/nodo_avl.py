class NodoAVL:
    def __init__(self, dato):
        self.__dato = dato
        self.__altura = 1
        self.__izquierdo = None
        self.__derecho = None

    def get_dato(self):
        return self.__dato

    def set_dato(self, dato):
        self.__dato = dato

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_izquierdo(self):
        return self.__izquierdo

    def set_izquierdo(self, nodo):
        self.__izquierdo = nodo

    def get_derecho(self):
        return self.__derecho

    def set_derecho(self, nodo):
        self.__derecho = nodo