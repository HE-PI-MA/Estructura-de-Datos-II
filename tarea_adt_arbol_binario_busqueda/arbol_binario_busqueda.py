"""Implementación de un Árbol Binario de Búsqueda (ABB)."""

from collections import deque

if __package__:
    from .nodo import Nodo
else:
    from nodo import Nodo


class ArbolBinarioBusqueda:
    """Representa un ABB sin valores duplicados."""

    def __init__(self):
        self.__raiz = None

    def get_raiz(self):
        """Devuelve la raíz del árbol."""
        return self.__raiz

    def set_raiz(self, nodo):
        """Asigna un objeto Nodo o None como raíz."""
        if nodo is not None and not isinstance(nodo, Nodo):
            raise TypeError("La raíz debe ser un objeto Nodo o None")
        self.__raiz = nodo

    def Insertar(self, x):
        """Inserta ``x`` respetando la propiedad ABB.

        Devuelve True si se insertó y False si el valor ya existía.
        """
        if x is None:
            raise ValueError("No se puede insertar None en el árbol")

        nuevo = Nodo(x)
        if self.__raiz is None:
            self.__raiz = nuevo
            return True

        actual = self.__raiz
        while True:
            dato_actual = actual.get_dato()
            try:
                es_menor = x < dato_actual
                es_mayor = x > dato_actual
            except TypeError as error:
                raise TypeError(
                    "Los datos del árbol deben poder compararse entre sí"
                ) from error

            if es_menor:
                if actual.get_izquierdo() is None:
                    actual.set_izquierdo(nuevo)
                    return True
                actual = actual.get_izquierdo()
            elif es_mayor:
                if actual.get_derecho() is None:
                    actual.set_derecho(nuevo)
                    return True
                actual = actual.get_derecho()
            else:
                return False

    def Buscar(self, x):
        """Busca ``x`` usando la propiedad ABB.

        Devuelve el Nodo encontrado o None cuando el valor no existe.
        """
        actual = self.__raiz

        while actual is not None:
            dato_actual = actual.get_dato()
            try:
                es_menor = x < dato_actual
                es_mayor = x > dato_actual
            except TypeError as error:
                raise TypeError(
                    "El valor buscado debe poder compararse con los datos"
                ) from error

            if es_menor:
                actual = actual.get_izquierdo()
            elif es_mayor:
                actual = actual.get_derecho()
            else:
                return actual

        return None

    def EsHoja(self, nodo):
        """Indica si ``nodo`` existe y no tiene hijos."""
        if nodo is None:
            return False
        if not isinstance(nodo, Nodo):
            raise TypeError("Se esperaba un objeto Nodo o None")
        return (
            nodo.get_izquierdo() is None
            and nodo.get_derecho() is None
        )

    def Altura(self):
        """Devuelve la altura del árbol calculada recursivamente.

        La altura de un árbol vacío es -1 y la de un árbol con solo la raíz
        es 0.
        """
        return self.__altura(self.__raiz)

    def Cantidad(self):
        """Devuelve recursivamente la cantidad total de nodos."""
        return self.__cantidad(self.__raiz)

    def Amplitud(self):
        """Devuelve el máximo número de nodos presentes en un mismo nivel."""
        if self.__raiz is None:
            return 0

        amplitud_maxima = 0
        pendientes = deque([self.__raiz])

        while pendientes:
            cantidad_nivel = len(pendientes)
            amplitud_maxima = max(amplitud_maxima, cantidad_nivel)

            for _ in range(cantidad_nivel):
                actual = pendientes.popleft()
                if actual.get_izquierdo() is not None:
                    pendientes.append(actual.get_izquierdo())
                if actual.get_derecho() is not None:
                    pendientes.append(actual.get_derecho())

        return amplitud_maxima

    def InOrden(self):
        """Devuelve los datos en orden izquierdo, raíz, derecho."""
        recorrido = []
        self.__inorden(self.__raiz, recorrido)
        return recorrido

    def PreOrden(self):
        """Devuelve los datos en orden raíz, izquierdo, derecho."""
        recorrido = []
        self.__preorden(self.__raiz, recorrido)
        return recorrido

    def PostOrden(self):
        """Devuelve los datos en orden izquierdo, derecho, raíz."""
        recorrido = []
        self.__postorden(self.__raiz, recorrido)
        return recorrido

    def __altura(self, nodo):
        if nodo is None:
            return -1

        altura_izquierda = self.__altura(nodo.get_izquierdo())
        altura_derecha = self.__altura(nodo.get_derecho())
        return 1 + max(altura_izquierda, altura_derecha)

    def __cantidad(self, nodo):
        if nodo is None:
            return 0

        return (
            1
            + self.__cantidad(nodo.get_izquierdo())
            + self.__cantidad(nodo.get_derecho())
        )

    def __inorden(self, nodo, recorrido):
        if nodo is None:
            return

        self.__inorden(nodo.get_izquierdo(), recorrido)
        recorrido.append(nodo.get_dato())
        self.__inorden(nodo.get_derecho(), recorrido)

    def __preorden(self, nodo, recorrido):
        if nodo is None:
            return

        recorrido.append(nodo.get_dato())
        self.__preorden(nodo.get_izquierdo(), recorrido)
        self.__preorden(nodo.get_derecho(), recorrido)

    def __postorden(self, nodo, recorrido):
        if nodo is None:
            return

        self.__postorden(nodo.get_izquierdo(), recorrido)
        self.__postorden(nodo.get_derecho(), recorrido)
        recorrido.append(nodo.get_dato())

    def EstaVacio(self):
        """Indica si el árbol no contiene nodos."""
        return self.__raiz is None


    def Raiz(self):
        """Devuelve el dato almacenado en la raíz."""
        if self.__raiz is None:
            return None

        return self.__raiz.get_dato()


    def Minimo(self):
        """Devuelve el menor valor almacenado en el árbol."""
        if self.__raiz is None:
            return None

        actual = self.__raiz

        while actual.get_izquierdo() is not None:
            actual = actual.get_izquierdo()

        return actual.get_dato()


    def Maximo(self):
        """Devuelve el mayor valor almacenado en el árbol."""
        if self.__raiz is None:
            return None

        actual = self.__raiz

        while actual.get_derecho() is not None:
            actual = actual.get_derecho()

        return actual.get_dato()


    def Eliminar(self, x):
        """Elimina un valor del ABB."""

        self.__raiz = self.__eliminar(self.__raiz, x)


    def __eliminar(self, nodo, x):

        if nodo is None:
            return None


        if x < nodo.get_dato():

            nodo.set_izquierdo(
                self.__eliminar(
                    nodo.get_izquierdo(),
                    x
                )
            )


        elif x > nodo.get_dato():

            nodo.set_derecho(
                self.__eliminar(
                    nodo.get_derecho(),
                    x
                )
            )


        else:

            # Caso 1: nodo hoja
            if (
                nodo.get_izquierdo() is None
                and nodo.get_derecho() is None
            ):
                return None


            # Caso 2: solo hijo derecho
            if nodo.get_izquierdo() is None:
                return nodo.get_derecho()


            # Caso 2: solo hijo izquierdo
            if nodo.get_derecho() is None:
                return nodo.get_izquierdo()


            # Caso 3: dos hijos
            sucesor = self.__minimo_nodo(
                nodo.get_derecho()
            )

            nodo.set_dato(
                sucesor.get_dato()
            )

            nodo.set_derecho(
                self.__eliminar(
                    nodo.get_derecho(),
                    sucesor.get_dato()
                )
            )


        return nodo


    def __minimo_nodo(self, nodo):

        actual = nodo

        while actual.get_izquierdo() is not None:
            actual = actual.get_izquierdo()

        return actual

