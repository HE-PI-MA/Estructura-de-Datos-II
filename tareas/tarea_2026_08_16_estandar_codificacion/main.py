"""Demuestra el uso de todos los getters y setters de la práctica."""

if __package__:
    from .arbol_binario import ArbolBinario
    from .nodo import Nodo
else:
    from arbol_binario import ArbolBinario
    from nodo import Nodo


def main():
    """Construye un árbol y consulta y modifica sus atributos."""
    arbol = ArbolBinario()
    print("Árbol vacío:", arbol.get_raiz() is None)

    raiz = Nodo(50)
    raiz.set_izquierdo(Nodo(30))
    raiz.set_derecho(Nodo(70))
    arbol.set_raiz(raiz)

    print("\nÁrbol creado con setters:")
    print("Raíz:", arbol.get_raiz().get_dato())
    print("Hijo izquierdo:", raiz.get_izquierdo().get_dato())
    print("Hijo derecho:", raiz.get_derecho().get_dato())

    raiz.get_izquierdo().set_dato(25)
    print("\nNuevo dato del hijo izquierdo:",
          raiz.get_izquierdo().get_dato())

    raiz.set_derecho(None)
    print("Hijo derecho retirado:", raiz.get_derecho() is None)

    raiz.set_izquierdo(None)
    print("Hijo izquierdo retirado:", raiz.get_izquierdo() is None)

    arbol.set_raiz(None)
    print("Árbol vacío nuevamente:", arbol.get_raiz() is None)


if __name__ == "__main__":
    main()
