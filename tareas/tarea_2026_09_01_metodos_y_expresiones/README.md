# Árbol binario: implementación de métodos

Esta carpeta contiene una práctica independiente con dos formas de representar
un árbol binario general y una práctica adicional de árboles de expresiones.
Las inserciones se hacen **por nivel, de izquierda a derecha**. Por tanto, estos
árboles no son árboles binarios de búsqueda (ABB).

## Árbol binario estático

`ArbolBinarioEstatico` guarda los datos en una lista de tamaño fijo. La capacidad
se configura al crear el objeto:

```python
from arbol_estatico import ArbolBinarioEstatico

arbol = ArbolBinarioEstatico(capacidad=7)
arbol.InsertarNodo("A")
```

La raíz ocupa el índice `0`. Para un nodo situado en el índice `i`:

- hijo izquierdo: `2 * i + 1`
- hijo derecho: `2 * i + 2`

`InsertarNodo` devuelve el índice ocupado. Si el arreglo está lleno, produce un
`OverflowError`. El valor `None` se reserva para representar posiciones vacías.

## Árbol binario dinámico

`ArbolBinarioDinamico` enlaza objetos `Nodo`. Cada nodo tiene los atributos
públicos `dato`, `izquierdo` y `derecho`:

```python
from arbol_dinamico import ArbolBinarioDinamico

arbol = ArbolBinarioDinamico()
nodo_a = arbol.InsertarNodo("A")
```

`InsertarNodo` devuelve el nuevo objeto `Nodo`. No existe una capacidad máxima
predefinida: se crean nodos mientras haya memoria disponible.

## Diferencias entre las representaciones

| Característica | Estática | Dinámica |
| --- | --- | --- |
| Almacenamiento | Lista de tamaño fijo | Objetos `Nodo` enlazados |
| Ubicación de hijos | Fórmulas sobre índices | Referencias `izquierdo` y `derecho` |
| Capacidad | Se define al crear el árbol | Crece según se insertan nodos |
| Resultado de `InsertarNodo` | Índice insertado | Nuevo objeto `Nodo` |
| Resultado de `BuscarX` | Índice encontrado o `None` | Nodo encontrado o `None` |

## Métodos implementados

Las dos versiones ofrecen exactamente estos nombres:

- `InsertarNodo(x)`: inserta por nivel, de izquierda a derecha.
- `EsVacio()`: devuelve `True` cuando no hay nodos.
- `EsHoja()`: sin argumento comprueba la raíz. También acepta un índice en la
  versión estática o un objeto `Nodo` en la dinámica.
- `BuscarX(x)`: busca el primer dato igual a `x`.
- `InOrden()`: devuelve una lista en orden izquierdo, raíz, derecho.
- `PostOrden()`: devuelve una lista en orden izquierdo, derecho, raíz.
- `PreOrden()`: devuelve una lista en orden raíz, izquierdo, derecho.

Por ejemplo, al insertar `A, B, C, D, E, F, G`, los recorridos son:

```text
Preorden:  A B D E C F G
Inorden:   D B E A F C G
Postorden: D E B F G C A
```

## Árbol de expresiones

`ArbolExpresiones` acepta operandos alfanuméricos de un carácter, los operadores
`+`, `-`, `*`, `/` y paréntesis. El proceso es:

1. Quitar espacios y validar la expresión infija.
2. Convertirla a posfija con una pila, respetando paréntesis y precedencia.
3. Leer la posfija y construir el árbol con otra pila de nodos.
4. Obtener los recorridos preorden, inorden y postorden.

Ejemplo:

```text
Expresión infija: (A+B)*C
Expresión posfija: AB+C*
Preorden:  * + A B C
Inorden:   A + B * C
Postorden: A B + C *
```

El recorrido postorden coincide con la expresión posfija. Entradas como `A+`,
`A++B`, `(A+B`, `()` o `A$B` se rechazan con un mensaje que explica el problema.
No se incluyen operadores unarios; por ejemplo, `-A` no es válido en esta
versión.

## Ejecución de los ejemplos

Desde la raíz del repositorio, ejecutar los tres ejemplos con una expresión dada:

```bash
python tareas/tarea_2026_09_01_metodos_y_expresiones/main.py "(A+B)*C"
```

Si se omite la expresión, el programa la solicita por consola:

```bash
python tareas/tarea_2026_09_01_metodos_y_expresiones/main.py
```

También se puede ejecutar solamente la práctica de expresiones:

```bash
python tareas/tarea_2026_09_01_metodos_y_expresiones/arbol_expresiones.py
```

En Windows, `py` puede usarse en lugar de `python` si ese es el lanzador
configurado.

## Ejecución de las pruebas

La suite usa únicamente `unittest`, incluido en Python:

```bash
python -m unittest tareas.tarea_2026_09_01_metodos_y_expresiones.tests -v
```

También se admite el descubrimiento automático desde la raíz:

```bash
python -m unittest discover -v
```

Las pruebas comprueban árboles vacíos, inserción, búsquedas existentes e
inexistentes, nodos hoja y no hoja, los tres recorridos, la capacidad estática,
la conversión infija-posfija y varias expresiones incorrectas.

## Archivos

- `arbol_estatico.py`: implementación con arreglo fijo.
- `arbol_dinamico.py`: clases `Nodo` y `ArbolBinarioDinamico`.
- `arbol_expresiones.py`: conversión y árbol de expresiones.
- `main.py`: ejemplos integrados.
- `tests.py`: pruebas automatizadas.
- `__init__.py`: permite importar la carpeta como un paquete de Python.
