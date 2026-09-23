"""Ejemplo reproducible y menú opcional para practicar los métodos."""

import argparse

if __package__:
    from .arbol_mvias import ArbolMVias
else:
    from arbol_mvias import ArbolMVias


def mostrar(arbol):
    arbol.imprimir()
    print("InOrden:", arbol.InOrden())
    print("PreOrden:", arbol.PreOrden())
    print("PostOrden:", arbol.PostOrden())
    print("BFS (claves por nodo):", arbol.PorNiveles())
    print("Altura:", arbol.Altura())
    print("Nodos:", arbol.Cantidad(), "Claves:", arbol.CantidadClaves())
    print("Hojas:", arbol.CantidadHojas(), "Amplitud:", arbol.Amplitud())
    print("Mínimo:", arbol.Minimo(), "Máximo:", arbol.Maximo())
    print("Balanceado por alturas:", arbol.EsBalanceado())
    print("Estructura válida:", arbol.validar())


def menu(arbol):
    while True:
        print("\n1. Insertar  2. Buscar  3. Eliminar  4. Mostrar  0. Salir")
        try:
            opcion = input("Opción: ").strip()
            if opcion == "0":
                return
            if opcion == "4":
                mostrar(arbol)
            elif opcion in ("1", "2", "3"):
                clave = int(input("Clave entera: "))
                if opcion == "1":
                    print(
                        "Insertado" if arbol.Insertar(clave) else "Ya existe"
                    )
                elif opcion == "2":
                    nodo = arbol.Buscar(clave)
                    print("No encontrado" if nodo is None else nodo)
                else:
                    print(
                        "Eliminado" if arbol.Eliminar(clave) else "No existe"
                    )
            else:
                print("Elige una opción entre 0 y 4.")
        except ValueError as error:
            print("Entrada inválida:", error)
        except (EOFError, KeyboardInterrupt):
            print("\nFin del programa.")
            return


def main():
    parser = argparse.ArgumentParser(description="Árbol M-vías de búsqueda")
    parser.add_argument("--orden", type=int, default=4)
    parser.add_argument("--menu", action="store_true")
    args = parser.parse_args()
    try:
        arbol = ArbolMVias(args.orden)
    except (ValueError, TypeError) as error:
        parser.error(str(error))

    if args.menu:
        menu(arbol)
        return

    valores = [50, 25, 75, 10, 30, 60, 90, 5, 15, 27, 35]
    print(f"ÁRBOL M-VÍAS DE ORDEN {args.orden}")
    print("Insertar:", valores)
    for clave in valores:
        arbol.Insertar(clave)
    mostrar(arbol)
    print("\nBuscar 30:", arbol.Buscar(30))
    print("Buscar 99:", arbol.Buscar(99))
    print("Insertar 30 repetido:", arbol.Insertar(30))
    print("Eliminar 25:", arbol.Eliminar(25))
    print("Eliminar 99 inexistente:", arbol.Eliminar(99))
    mostrar(arbol)


if __name__ == "__main__":
    main()
