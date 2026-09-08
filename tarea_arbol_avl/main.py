from arbol_avl import ArbolAVL


def mostrar(titulo, datos):
    print("\n" + titulo)
    print(datos)


arbol = ArbolAVL()

valores = [30, 20, 10, 25, 40, 50, 5]

print("=== ARBOL AVL ===")

print("\nInsertando valores:")
print(valores)

for valor in valores:
    arbol.insertar(valor)

mostrar("Recorrido InOrden:", arbol.inorden())
mostrar("Recorrido PreOrden:", arbol.preorden())
mostrar("Recorrido PostOrden:", arbol.postorden())

print("\nCantidad de nodos:")
print(arbol.cantidad())

print("\nAltura del árbol:")
print(arbol.altura())

print("\nBuscar 25:")
resultado = arbol.buscar(25)

if resultado:
    print("Encontrado:", resultado.get_dato())
else:
    print("No encontrado")

print("\nEliminar 20")

arbol.eliminar(20)

mostrar("InOrden después de eliminar:", arbol.inorden())

print("\nAltura después de eliminar:")
print(arbol.altura())
