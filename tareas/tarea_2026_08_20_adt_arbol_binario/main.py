if __package__:
    from .arbol import Arbol
else:
    from arbol import Arbol


def main():
    arbol = Arbol()

    tablero_raiz = [
        ["X", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    tablero_izquierdo = [
        ["X", "O", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    tablero_derecho = [
        ["X", "", ""],
        ["", "O", ""],
        ["", "", ""]
    ]

    tablero_izquierdo_2 = [
        ["X", "O", "X"],
        ["", "", ""],
        ["", "", ""]
    ]

    raiz = arbol.insertar_raiz(tablero_raiz)

    izquierdo = arbol.agregar_izquierdo(
        raiz,
        tablero_izquierdo
    )

    arbol.agregar_derecho(
        raiz,
        tablero_derecho
    )

    arbol.agregar_izquierdo(
        izquierdo,
        tablero_izquierdo_2
    )

    print("RECORRIDO PREORDEN")
    print()
    arbol.recorrido_preorden(arbol.get_raiz())

    print("RECORRIDO INORDEN")
    print()
    arbol.recorrido_inorden(arbol.get_raiz())

    print("RECORRIDO POSTORDEN")
    print()
    arbol.recorrido_postorden(arbol.get_raiz())

    print("BUSQUEDA DE TABLERO")
    print()

    resultado = arbol.buscar_tablero(
        arbol.get_raiz(),
        tablero_derecho
    )

    if resultado is not None:
        print("Tablero encontrado:")
        resultado.mostrar_tablero()
    else:
        print("El tablero no existe en el arbol")


if __name__ == "__main__":
    main()