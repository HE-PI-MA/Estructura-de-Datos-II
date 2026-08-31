"""Ejemplos de uso de las tres implementaciones de la práctica."""

import argparse

if __package__:
    from .arbol_dinamico import ArbolBinarioDinamico
    from .arbol_estatico import ArbolBinarioEstatico
    from .arbol_expresiones import ArbolExpresiones
else:
    from arbol_dinamico import ArbolBinarioDinamico
    from arbol_estatico import ArbolBinarioEstatico
    from arbol_expresiones import ArbolExpresiones


DATOS_EJEMPLO = ["A", "B", "C", "D", "E", "F", "G"]


def mostrar_recorridos(arbol):
    """Imprime los tres recorridos de un árbol."""
    print(f"Preorden:  {arbol.PreOrden()}")
    print(f"Inorden:   {arbol.InOrden()}")
    print(f"Postorden: {arbol.PostOrden()}")


def ejemplo_estatico():
    """Crea y muestra un árbol almacenado en un arreglo fijo."""
    arbol = ArbolBinarioEstatico(capacidad=10)
    for dato in DATOS_EJEMPLO:
        arbol.InsertarNodo(dato)

    print("=== ÁRBOL BINARIO ESTÁTICO ===")
    print(f"Arreglo: {arbol.nodos}")
    print(f"Posición de E: {arbol.BuscarX('E')}")
    print(f"¿La raíz es hoja?: {arbol.EsHoja()}")
    print(f"¿El nodo del índice 3 es hoja?: {arbol.EsHoja(3)}")
    mostrar_recorridos(arbol)


def ejemplo_dinamico():
    """Crea y muestra un árbol formado por objetos Nodo."""
    arbol = ArbolBinarioDinamico()
    for dato in DATOS_EJEMPLO:
        arbol.InsertarNodo(dato)

    nodo_e = arbol.BuscarX("E")
    print("\n=== ÁRBOL BINARIO DINÁMICO ===")
    print(f"Dato encontrado: {nodo_e.dato if nodo_e else None}")
    print(f"¿La raíz es hoja?: {arbol.EsHoja()}")
    print(f"¿El nodo E es hoja?: {arbol.EsHoja(nodo_e)}")
    mostrar_recorridos(arbol)


def ejemplo_expresion(expresion):
    """Construye un árbol de expresión y muestra sus recorridos."""
    arbol = ArbolExpresiones()
    print("\n=== ÁRBOL DE EXPRESIONES ===")

    try:
        arbol.Construir(expresion)
    except (TypeError, ValueError) as error:
        print(f"Expresión incorrecta: {error}")
        return

    print(f"Expresión infija: {arbol.ObtenerInfija()}")
    print(f"Expresión posfija: {arbol.ObtenerPosfija()}")
    print(f"Preorden:  {' '.join(arbol.PreOrden())}")
    print(f"Inorden:   {' '.join(arbol.InOrden())}")
    print(f"Postorden: {' '.join(arbol.PostOrden())}")
    print(f"Árbol como expresión: {arbol.InOrdenConParentesis()}")


def main():
    parser = argparse.ArgumentParser(
        description="Ejemplos de árboles binarios estático y dinámico"
    )
    parser.add_argument(
        "expresion",
        nargs="?",
        help="expresión infija; si se omite, se solicita por consola",
    )
    argumentos = parser.parse_args()

    ejemplo_estatico()
    ejemplo_dinamico()

    expresion = argumentos.expresion
    if expresion is None:
        expresion = input("\nEscriba una expresión infija: ")
    ejemplo_expresion(expresion)


if __name__ == "__main__":
    main()
