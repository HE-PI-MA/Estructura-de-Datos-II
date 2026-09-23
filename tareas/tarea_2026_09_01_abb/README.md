# ADT Árbol Binario de Búsqueda

Esta práctica implementa un Árbol Binario de Búsqueda (ABB) en Python mediante
Programación Orientada a Objetos, encapsulamiento y métodos de acceso.

## ¿Qué es un Árbol Binario de Búsqueda?

Un árbol binario es una estructura en la que cada nodo puede tener, como
máximo, un hijo izquierdo y uno derecho. En un ABB se agrega una propiedad de
orden para cada nodo:

- todos los datos de su subárbol izquierdo son menores;
- todos los datos de su subárbol derecho son mayores.

Esta propiedad permite buscar un valor eligiendo solo uno de los dos caminos en
cada comparación. Los datos almacenados deben poder compararse entre sí.

## Diferencia respecto a un árbol binario general

Un árbol binario general no exige un orden entre los datos. Por ejemplo, puede
insertar por niveles para ocupar posiciones de izquierda a derecha. En cambio,
el ABB decide la posición de cada dato mediante comparaciones. Por esta razón,
el recorrido inorden de un ABB devuelve los datos de menor a mayor.

Esta implementación es independiente de las prácticas anteriores del
repositorio y no reutiliza directamente sus árboles binarios generales.

## Clase Nodo

La clase `Nodo`, ubicada en `nodo.py`, encapsula tres atributos privados:

- `__dato`: valor almacenado;
- `__izquierdo`: referencia al hijo izquierdo;
- `__derecho`: referencia al hijo derecho.

Ofrece los siguientes getters y setters:

- `get_dato()` y `set_dato(dato)`;
- `get_izquierdo()` y `set_izquierdo(nodo)`;
- `get_derecho()` y `set_derecho(nodo)`.

Los setters de los hijos aceptan únicamente un objeto `Nodo` o `None`.

## Clase ArbolBinarioBusqueda

La clase mantiene la raíz en el atributo privado `__raiz`. `get_raiz()` permite
consultarla y `set_raiz(nodo)` acepta un objeto `Nodo` o `None`.

### Insertar(x)

Compara el nuevo valor con cada nodo desde la raíz. Avanza a la izquierda si es
menor y a la derecha si es mayor. Devuelve `True` cuando inserta el dato. Los
duplicados se ignoran y producen `False`.

### Buscar(x)

Usa la propiedad ABB para recorrer solo el camino donde podría estar el dato.
Devuelve el objeto `Nodo` encontrado o `None` si no existe.

### EsHoja(nodo)

Devuelve `True` cuando el nodo indicado no tiene hijo izquierdo ni derecho. Si
se recibe `None`, devuelve `False`.

### Altura()

Calcula la altura recursivamente. Se usa la siguiente convención:

- árbol vacío: altura `-1`;
- árbol con solo la raíz: altura `0`.

Por tanto, la altura equivale a la cantidad de aristas del camino más largo
desde la raíz hasta una hoja.

### Cantidad()

Cuenta recursivamente todos los nodos del árbol. Un árbol vacío tiene cantidad
`0`.

### Amplitud()

La amplitud se define como el máximo número de nodos existentes en un mismo
nivel. Se calcula mediante un recorrido por niveles con `collections.deque`.
Un árbol vacío tiene amplitud `0`.

Para el árbol del ejemplo, los niveles contienen `1`, `2` y `4` nodos, de modo
que su amplitud es `4`:

```text
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

## Recorridos

- `InOrden()`: izquierdo, raíz, derecho. Produce datos ordenados.
- `PreOrden()`: raíz, izquierdo, derecho.
- `PostOrden()`: izquierdo, derecho, raíz.

Al insertar `50, 30, 70, 20, 40, 60, 80`, se obtiene:

```text
Inorden:   [20, 30, 40, 50, 60, 70, 80]
Preorden:  [50, 30, 20, 40, 70, 60, 80]
Postorden: [20, 40, 30, 60, 80, 70, 50]
```

## Ejecución

Desde la raíz del repositorio:

```bash
python tareas/tarea_2026_09_01_abb/main.py
```

El ejemplo muestra el árbol vacío, inserciones, un duplicado, búsquedas, nodos
hoja y no hoja, altura, cantidad, amplitud y los tres recorridos.

## Pruebas

Las pruebas utilizan únicamente `unittest`:

```bash
python -m unittest tareas.tarea_2026_09_01_abb.tests -v
```

Para comprobar que todos los archivos pueden compilarse:

```bash
python -m compileall tarea_adt_arbol_binario_busqueda
```

## Archivos

- `nodo.py`: clase `Nodo` encapsulada.
- `arbol_binario_busqueda.py`: clase `ArbolBinarioBusqueda`.
- `main.py`: demostración completa.
- `tests.py`: pruebas automatizadas.
- `__init__.py`: definición del paquete de Python.
