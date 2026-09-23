# Árbol AVL

## Descripción

Un árbol AVL es un árbol binario de búsqueda autobalanceado que mantiene una altura equilibrada después de cada inserción o eliminación.

## Característica principal

Cada nodo mantiene un factor de balance:

Factor de balance = altura del subárbol izquierdo - altura del subárbol derecho

El valor permitido debe estar entre -1, 0 y 1.

Cuando el balance se pierde se aplican rotaciones.

## Implementación

La implementación contiene:

- Nodo AVL.
- Inserción con balance automático.
- Búsqueda.
- Eliminación.
- Rotaciones simples.
- Rotaciones dobles.
- Recorridos InOrden, PreOrden y PostOrden.

## Rotaciones implementadas

### LL

Rotación simple derecha.

### RR

Rotación simple izquierda.

### LR

Rotación izquierda seguida de derecha.

### RL

Rotación derecha seguida de izquierda.

## Ejecución

Ejecutar:

python main.py

Pruebas:

python -m unittest tests -v

## Resultados

La implementación fue comprobada mediante pruebas unitarias usando unittest.
