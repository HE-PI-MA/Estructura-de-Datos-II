class Nodo:
    def __init__(self, tablero=None):
        if tablero is None:
            tablero = [
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]

        self.__validar_tablero(tablero)

        self.__tablero = tablero
        self.__izquierdo = None
        self.__derecho = None

    def __validar_tablero(self, tablero):
        if not isinstance(tablero, list) or len(tablero) != 3:
            raise ValueError("El tablero debe ser una matriz de 3x3")

        for fila in tablero:
            if not isinstance(fila, list) or len(fila) != 3:
                raise ValueError("El tablero debe ser una matriz de 3x3")

    def get_tablero(self):
        return self.__tablero

    def set_tablero(self, tablero):
        self.__validar_tablero(tablero)
        self.__tablero = tablero

    def get_izquierdo(self):
        return self.__izquierdo

    def set_izquierdo(self, nodo):
        self.__izquierdo = nodo

    def get_derecho(self):
        return self.__derecho

    def set_derecho(self, nodo):
        self.__derecho = nodo

    def mostrar_tablero(self):
        for fila in self.__tablero:
            print(" | ".join(celda if celda != "" else " " for celda in fila))
        print()