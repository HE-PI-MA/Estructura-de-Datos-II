"""Conversión infija-posfija y construcción de un árbol de expresión."""

if __package__:
    from .arbol_dinamico import Nodo
else:
    from arbol_dinamico import Nodo


class ArbolExpresiones:
    """Construye un árbol a partir de una expresión infija válida."""

    __prioridad = {"+": 1, "-": 1, "*": 2, "/": 2}

    def __init__(self):
        self.raiz = None
        self.__infija = ""
        self.__posfija = ""

    def Construir(self, expresion):
        """Valida la expresión, la convierte a posfija y construye el árbol."""
        posfija, infija_limpia = self.__convertir_a_posfija(expresion)
        nueva_raiz = self.__construir_desde_posfija(posfija)

        self.raiz = nueva_raiz
        self.__infija = infija_limpia
        self.__posfija = posfija
        return self.raiz

    def InfijaAPosfija(self, expresion):
        """Devuelve la versión posfija sin modificar el árbol actual."""
        posfija, _ = self.__convertir_a_posfija(expresion)
        return posfija

    def ObtenerInfija(self):
        """Devuelve la última expresión infija construida."""
        return self.__infija

    def ObtenerPosfija(self):
        """Devuelve la expresión posfija del árbol actual."""
        return self.__posfija

    def InOrden(self):
        """Devuelve el recorrido inorden del árbol de expresión."""
        recorrido = []
        self.__inorden(self.raiz, recorrido)
        return recorrido

    def PostOrden(self):
        """Devuelve el recorrido postorden del árbol de expresión."""
        recorrido = []
        self.__postorden(self.raiz, recorrido)
        return recorrido

    def PreOrden(self):
        """Devuelve el recorrido preorden del árbol de expresión."""
        recorrido = []
        self.__preorden(self.raiz, recorrido)
        return recorrido

    def InOrdenConParentesis(self):
        """Reconstruye la expresión del árbol usando paréntesis explícitos."""
        return self.__inorden_con_parentesis(self.raiz)

    def __convertir_a_posfija(self, expresion):
        if not isinstance(expresion, str):
            raise TypeError("La expresión debe ser una cadena de texto")

        infija = "".join(expresion.split())
        if not infija:
            raise ValueError("La expresión no puede estar vacía")

        salida = []
        operadores = []
        espera_operando = True

        for simbolo in infija:
            if simbolo.isalnum():
                if not espera_operando:
                    raise ValueError(
                        "Falta un operador entre dos operandos"
                    )
                salida.append(simbolo)
                espera_operando = False
            elif simbolo == "(":
                if not espera_operando:
                    raise ValueError("Falta un operador antes de '('")
                operadores.append(simbolo)
            elif simbolo == ")":
                if espera_operando:
                    raise ValueError("Falta un operando antes de ')'")

                while operadores and operadores[-1] != "(":
                    salida.append(operadores.pop())
                if not operadores:
                    raise ValueError("Hay un paréntesis ')' sin apertura")
                operadores.pop()
                espera_operando = False
            elif simbolo in self.__prioridad:
                if espera_operando:
                    raise ValueError(
                        f"Falta un operando antes del operador '{simbolo}'"
                    )

                while (
                    operadores
                    and operadores[-1] != "("
                    and self.__prioridad[operadores[-1]]
                    >= self.__prioridad[simbolo]
                ):
                    salida.append(operadores.pop())
                operadores.append(simbolo)
                espera_operando = True
            else:
                raise ValueError(f"Símbolo no permitido: '{simbolo}'")

        if espera_operando:
            raise ValueError("La expresión termina sin un operando")

        while operadores:
            operador = operadores.pop()
            if operador == "(":
                raise ValueError("Hay un paréntesis '(' sin cierre")
            salida.append(operador)

        return "".join(salida), infija

    def __construir_desde_posfija(self, posfija):
        pila = []

        for simbolo in posfija:
            if simbolo.isalnum():
                pila.append(Nodo(simbolo))
                continue

            if len(pila) < 2:
                raise ValueError("La expresión no tiene suficientes operandos")

            derecho = pila.pop()
            izquierdo = pila.pop()
            operador = Nodo(simbolo)
            operador.izquierdo = izquierdo
            operador.derecho = derecho
            pila.append(operador)

        if len(pila) != 1:
            raise ValueError("La expresión no forma un árbol válido")
        return pila[0]

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

    def __inorden_con_parentesis(self, nodo):
        if nodo is None:
            return ""
        if nodo.izquierdo is None and nodo.derecho is None:
            return str(nodo.dato)

        izquierdo = self.__inorden_con_parentesis(nodo.izquierdo)
        derecho = self.__inorden_con_parentesis(nodo.derecho)
        return f"({izquierdo}{nodo.dato}{derecho})"


def main():
    """Solicita una expresión y muestra su conversión y recorridos."""
    expresion = input("Escriba una expresión infija: ")
    arbol = ArbolExpresiones()

    try:
        arbol.Construir(expresion)
    except (TypeError, ValueError) as error:
        print(f"Expresión incorrecta: {error}")
        return

    print(f"Expresión infija: {arbol.ObtenerInfija()}")
    print(f"Expresión posfija: {arbol.ObtenerPosfija()}")
    print(f"Preorden: {' '.join(arbol.PreOrden())}")
    print(f"Inorden: {' '.join(arbol.InOrden())}")
    print(f"Postorden: {' '.join(arbol.PostOrden())}")


if __name__ == "__main__":
    main()
