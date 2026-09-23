if __package__:
    from .nodo_avl import NodoAVL
else:
    from nodo_avl import NodoAVL


class ArbolAVL:
    def __init__(self):
        self.__raiz = None

    def get_raiz(self):
        return self.__raiz

    def set_raiz(self, nodo):
        self.__raiz = nodo

    def altura_nodo(self, nodo):
        if nodo is None:
            return 0
        return nodo.get_altura()

    def actualizar_altura(self, nodo):
        if nodo:
            altura_izq = self.altura_nodo(nodo.get_izquierdo())
            altura_der = self.altura_nodo(nodo.get_derecho())
            nodo.set_altura(max(altura_izq, altura_der) + 1)

    def factor_balance(self, nodo):
        if nodo is None:
            return 0

        return (
            self.altura_nodo(nodo.get_izquierdo())
            - self.altura_nodo(nodo.get_derecho())
        )

    def rotacion_derecha(self, y):
        x = y.get_izquierdo()
        t2 = x.get_derecho()

        x.set_derecho(y)
        y.set_izquierdo(t2)

        self.actualizar_altura(y)
        self.actualizar_altura(x)

        return x

    def rotacion_izquierda(self, x):
        y = x.get_derecho()
        t2 = y.get_izquierdo()

        y.set_izquierdo(x)
        x.set_derecho(t2)

        self.actualizar_altura(x)
        self.actualizar_altura(y)

        return y

    def insertar(self, dato):
        self.__raiz = self._insertar(self.__raiz, dato)

    def _insertar(self, nodo, dato):
        if nodo is None:
            return NodoAVL(dato)

        if dato < nodo.get_dato():
            nodo.set_izquierdo(
                self._insertar(nodo.get_izquierdo(), dato)
            )
        elif dato > nodo.get_dato():
            nodo.set_derecho(
                self._insertar(nodo.get_derecho(), dato)
            )
        else:
            return nodo

        self.actualizar_altura(nodo)

        balance = self.factor_balance(nodo)

        # Caso izquierda izquierda
        if balance > 1 and dato < nodo.get_izquierdo().get_dato():
            return self.rotacion_derecha(nodo)

        # Caso derecha derecha
        if balance < -1 and dato > nodo.get_derecho().get_dato():
            return self.rotacion_izquierda(nodo)

        # Caso izquierda derecha
        if balance > 1 and dato > nodo.get_izquierdo().get_dato():
            nodo.set_izquierdo(
                self.rotacion_izquierda(nodo.get_izquierdo())
            )
            return self.rotacion_derecha(nodo)

        # Caso derecha izquierda
        if balance < -1 and dato < nodo.get_derecho().get_dato():
            nodo.set_derecho(
                self.rotacion_derecha(nodo.get_derecho())
            )
            return self.rotacion_izquierda(nodo)

        return nodo

    def buscar(self, dato):
        return self._buscar(self.__raiz, dato)

    def _buscar(self, nodo, dato):
        if nodo is None:
            return None

        if dato == nodo.get_dato():
            return nodo

        if dato < nodo.get_dato():
            return self._buscar(nodo.get_izquierdo(), dato)

        return self._buscar(nodo.get_derecho(), dato)


    def es_hoja(self, nodo):
        if nodo is None:
            return False

        return (
            nodo.get_izquierdo() is None
            and nodo.get_derecho() is None
        )

    def cantidad(self):
        return self._cantidad(self.__raiz)

    def _cantidad(self, nodo):
        if nodo is None:
            return 0

        return (
            1
            + self._cantidad(nodo.get_izquierdo())
            + self._cantidad(nodo.get_derecho())
        )

    def inorden(self):
        resultado = []
        self._inorden(self.__raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.get_izquierdo(), resultado)
            resultado.append(nodo.get_dato())
            self._inorden(nodo.get_derecho(), resultado)

    def preorden(self):
        resultado = []
        self._preorden(self.__raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.get_dato())
            self._preorden(nodo.get_izquierdo(), resultado)
            self._preorden(nodo.get_derecho(), resultado)

    def postorden(self):
        resultado = []
        self._postorden(self.__raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.get_izquierdo(), resultado)
            self._postorden(nodo.get_derecho(), resultado)
            resultado.append(nodo.get_dato())


    def eliminar(self, dato):
        self.__raiz = self._eliminar(self.__raiz, dato)

    def _nodo_minimo(self, nodo):
        actual = nodo

        while actual.get_izquierdo() is not None:
            actual = actual.get_izquierdo()

        return actual

    def _eliminar(self, nodo, dato):
        if nodo is None:
            return None

        if dato < nodo.get_dato():
            nodo.set_izquierdo(
                self._eliminar(nodo.get_izquierdo(), dato)
            )

        elif dato > nodo.get_dato():
            nodo.set_derecho(
                self._eliminar(nodo.get_derecho(), dato)
            )

        else:

            if nodo.get_izquierdo() is None:
                return nodo.get_derecho()

            if nodo.get_derecho() is None:
                return nodo.get_izquierdo()

            sucesor = self._nodo_minimo(
                nodo.get_derecho()
            )

            nodo.set_dato(
                sucesor.get_dato()
            )

            nodo.set_derecho(
                self._eliminar(
                    nodo.get_derecho(),
                    sucesor.get_dato()
                )
            )

        self.actualizar_altura(nodo)

        balance = self.factor_balance(nodo)

        # Caso izquierda izquierda
        if balance > 1 and self.factor_balance(
            nodo.get_izquierdo()
        ) >= 0:
            return self.rotacion_derecha(nodo)

        # Caso izquierda derecha
        if balance > 1 and self.factor_balance(
            nodo.get_izquierdo()
        ) < 0:
            nodo.set_izquierdo(
                self.rotacion_izquierda(
                    nodo.get_izquierdo()
                )
            )
            return self.rotacion_derecha(nodo)

        # Caso derecha derecha
        if balance < -1 and self.factor_balance(
            nodo.get_derecho()
        ) <= 0:
            return self.rotacion_izquierda(nodo)

        # Caso derecha izquierda
        if balance < -1 and self.factor_balance(
            nodo.get_derecho()
        ) > 0:
            nodo.set_derecho(
                self.rotacion_derecha(
                    nodo.get_derecho()
                )
            )
            return self.rotacion_izquierda(nodo)

        return nodo

    def altura(self):
        return self.altura_nodo(self.__raiz)

