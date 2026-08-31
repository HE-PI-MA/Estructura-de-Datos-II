"""Ejemplo de uso del ADT Árbol Binario de Búsqueda."""

if __package__:
    from .arbol_binario_busqueda import ArbolBinarioBusqueda
else:
    from arbol_binario_busqueda import ArbolBinarioBusqueda


VALORES = [50, 30, 70, 20, 40, 60, 80]


def main():
    """Construye un ABB y presenta sus operaciones principales."""
    arbol = ArbolBinarioBusqueda()

    print("=== ADT ÁRBOL BINARIO DE BÚSQUEDA ===")
    print(f"Árbol inicialmente vacío: {arbol.get_raiz() is None}")
    print(f"Altura inicial: {arbol.Altura()}")
    print(f"Cantidad inicial: {arbol.Cantidad()}")
    print(f"Amplitud inicial: {arbol.Amplitud()}")

    print(f"\nValores a insertar: {VALORES}")
    for valor in VALORES:
        insertado = arbol.Insertar(valor)
        print(f"Insertar {valor}: {insertado}")

    print(f"Insertar duplicado 40: {arbol.Insertar(40)}")

    buscado = 60
    encontrado = arbol.Buscar(buscado)
    print(f"\nBuscar {buscado}: {encontrado is not None}")
    if encontrado is not None:
        print(f"Dato del nodo encontrado: {encontrado.get_dato()}")

    inexistente = 99
    print(f"Buscar {inexistente}: {arbol.Buscar(inexistente)}")

    nodo_20 = arbol.Buscar(20)
    nodo_30 = arbol.Buscar(30)
    print(f"\n¿El nodo 20 es hoja?: {arbol.EsHoja(nodo_20)}")
    print(f"¿El nodo 30 es hoja?: {arbol.EsHoja(nodo_30)}")
    print(f"Altura: {arbol.Altura()}")
    print(f"Cantidad de nodos: {arbol.Cantidad()}")
    print(f"Amplitud máxima: {arbol.Amplitud()}")

    print(f"\nInorden: {arbol.InOrden()}")
    print(f"Preorden: {arbol.PreOrden()}")
    print(f"Postorden: {arbol.PostOrden()}")


if __name__ == "__main__":
    main()
