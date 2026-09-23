# Investigación: Árbol AVL

## 1. Introducción

Un árbol AVL es una estructura de datos basada en un árbol binario de búsqueda que incorpora un mecanismo de autoequilibrio. Fue creado por Georgy Adelson-Velsky y Evgenii Landis en 1962.

Su objetivo principal es mantener una altura mínima del árbol para garantizar operaciones eficientes de búsqueda, inserción y eliminación.

## 2. Árbol Binario de Búsqueda (ABB)

Un árbol binario de búsqueda organiza sus elementos siguiendo estas reglas:

- Los valores menores que un nodo se almacenan en el subárbol izquierdo.
- Los valores mayores que un nodo se almacenan en el subárbol derecho.
- Cada nodo puede tener como máximo dos hijos.

El problema de un ABB tradicional es que puede volverse desbalanceado y comportarse como una lista enlazada.

## 3. Característica del Árbol AVL

Un árbol AVL mantiene equilibrado el árbol mediante el factor de balance.

La fórmula es:

Factor de balance = altura del hijo izquierdo - altura del hijo derecho

Los valores permitidos son:

- -1
- 0
- 1

Cuando el valor sale de este rango, el árbol realiza rotaciones para recuperar el equilibrio.

## 4. Rotaciones AVL

Las rotaciones son operaciones que modifican la estructura del árbol manteniendo el orden de búsqueda.

### 4.1 Rotación LL

Ocurre cuando un nodo se carga hacia la izquierda.

Se soluciona mediante una rotación simple derecha.

### 4.2 Rotación RR

Ocurre cuando un nodo se carga hacia la derecha.

Se soluciona mediante una rotación simple izquierda.

### 4.3 Rotación LR

Es una combinación de dos movimientos:

- Rotación izquierda en el hijo izquierdo.
- Rotación derecha en el nodo afectado.

### 4.4 Rotación RL

Es una combinación de:

- Rotación derecha en el hijo derecho.
- Rotación izquierda en el nodo afectado.

## 5. Complejidad Algorítmica

Gracias al equilibrio automático, las operaciones principales tienen una complejidad eficiente:

| Operación | Complejidad |
|---|---|
| Búsqueda | O(log n) |
| Inserción | O(log n) |
| Eliminación | O(log n) |

## 6. Implementación realizada

La implementación desarrollada contiene:

- Clase NodoAVL.
- Clase ArbolAVL.
- Inserción con balance automático.
- Rotaciones LL, RR, LR y RL.
- Búsqueda de elementos.
- Eliminación de nodos.
- Recorridos InOrden, PreOrden y PostOrden.
- Pruebas unitarias mediante unittest.

## 7. Conclusión

El árbol AVL permite mantener una estructura equilibrada evitando que un árbol binario de búsqueda pierda eficiencia. Mediante sus rotaciones automáticas garantiza tiempos de respuesta rápidos para grandes cantidades de datos.
