# Árbol M-vías: métodos vistos en ABB

Materia: Estructura de Datos II — INF310, grupo SA, UAGRM.
Cierre publicado: **23 de septiembre de 2026, 23:17**.
[Consigna](https://presencial.uagrm.edu.bo/mod/assign/view.php?id=1507186):
adaptar los métodos del ABB a un árbol M-vías, separar las clases y entregar ZIP.

## Archivos

- `nodo_mvias.py`: clase `NodoMVias`, claves, hijos, getters y setters.
- `arbol_mvias.py`: clase `ArbolMVias` y algoritmos.
- `main.py`: demostración y menú opcional.
- `tests.py`: pruebas automáticas.
- `__init__.py`: permite importar la tarea como paquete.

## Ejecución

Con Python 3, desde la carpeta extraída del ZIP:

```bash
python main.py
python main.py --menu --orden 4
python -m unittest tests -v
```

Desde la raíz del repositorio:

```bash
python tareas/tarea_2026_09_23_mvias_metodos/main.py
python -m unittest tareas.tarea_2026_09_23_mvias_metodos.tests -v
```

En Windows también puede utilizarse `py` en lugar de `python`.
No requiere dependencias externas. El menú recibe números enteros; la clase
también acepta cadenas de texto comparables entre sí.

## Estructura y reglas

Un árbol de orden `m` admite hasta `m - 1` claves en cada nodo y hasta `m` hijos.
Las claves se mantienen ordenadas, sin duplicados. Un nodo con `k` claves usa
los hijos de posiciones `0` hasta `k`. El hijo `0` contiene valores menores
que la primera clave; los hijos intermedios contienen valores entre claves;
el hijo `k` contiene valores mayores que la última clave.

Se sigue la base de [M-vías de la unidad 2 del docente](https://github.com/profjcp/INF310-EstructurasDatos2/blob/main/unidad2/ejemplos/02_arbol_mvias.py):
inserción sin división de nodos ni balanceo automático. Es un árbol M-vías de
búsqueda, no un árbol B. El orden mínimo es 2.

## Métodos

Los nombres en mayúsculas permiten reutilizar las llamadas del ABB anterior.
Los nombres en minúsculas siguen el estilo de Python y del ejemplo del docente.

| Método | Resultado |
| --- | --- |
| `get_raiz()`, `set_raiz(nodo)` | Consultar o asignar una raíz válida del mismo orden |
| `get_orden()`, `set_orden(m)` | Consultar el orden; modificarlo solo con el árbol vacío |
| `EstaVacio()`, `EsVacio()`, `esta_vacio()` | `True` si no hay raíz |
| `Raiz()`, `raiz()` | Lista con las claves de la raíz; `[]` si está vacío |
| `Insertar(x)`, `InsertarNodo(x)`, `insertar(x)` | `True` si se insertó; `False` si ya existía |
| `Buscar(x)`, `BuscarX(x)`, `obtener_nodo(x)` | Nodo que contiene la clave, o `None` |
| `buscar(x)` | Booleano, como en el ejemplo del docente |
| `Eliminar(x)`, `eliminar(x)` | `True` si eliminó la clave; `False` si no existía |
| `EsHoja(nodo)`, `es_hoja(nodo)` | Indica si el nodo existe y no tiene hijos |
| `Minimo()`, `Maximo()` / `minimo()`, `maximo()` | Clave extrema; `None` si está vacío |
| `Altura()`, `altura()` | Altura en aristas: vacío `-1`, una sola raíz `0` |
| `Cantidad()`, `cantidad()` | Cantidad de nodos físicos |
| `CantidadClaves()`, `cantidad_claves()`, `len(arbol)` | Cantidad total de claves |
| `CantidadHojas()`, `cantidad_hojas()` | Número de nodos sin hijos |
| `Amplitud()`, `amplitud()` | Máximo número de nodos físicos en un nivel |
| `InOrden()`, `en_orden()` | Lista de claves ordenadas |
| `PreOrden()`, `pre_orden()` | Recorrido preorden generalizado |
| `PostOrden()`, `post_orden()` | Recorrido postorden generalizado |
| `PorNiveles()`, `por_niveles()` | BFS; una lista de claves por nodo |
| `niveles()` | Nodos agrupados por profundidad |
| `EsBalanceado()`, `es_balanceado()` | Comprueba diferencia de altura máxima de 1 entre los hijos activos, incluyendo vacíos; no modifica el árbol |
| `validar()` | Comprueba rangos, capacidad, orden y ausencia de ciclos |
| `vaciar()` | Quita la raíz |
| `imprimir()` | Muestra los nodos por nivel en consola |

`Cantidad()` conserva el significado del ABB: contar nodos. En M-vías un nodo
puede guardar varias claves, por eso se ofrece además `CantidadClaves()`.
Los extremos de un árbol vacío siguen el criterio de la implementación del
estudiante: devuelven `None`.

El nodo ofrece `get_orden`, `set_orden`, `get_claves`, `set_claves`,
`get_clave`, `set_clave`, `get_hijos`, `set_hijos`, `get_hijo` y `set_hijo`.
Los getters de listas devuelven copias. Los setters verifican tipos y capacidad.
Para armar un árbol manualmente, construir primero sus nodos y luego usar
`set_raiz`, que comprueba los rangos completos. Cambiar manualmente los nodos de
un árbol ya enlazado puede romper esos rangos; `validar()` permite detectarlo.

## Cómo funcionan los algoritmos

**Insertar:** buscar el intervalo de la nueva clave. Si la hoja tiene espacio,
agregar la clave en orden. En otro caso, bajar al hijo correspondiente o crearlo.
Los nodos internos con espacio tras una eliminación conservan sus claves y se
continúa descendiendo para respetar los intervalos de los hijos.

**Buscar:** comparar con las claves del nodo. Si no aparece, seguir el hijo del
intervalo donde debería encontrarse; terminar al llegar a un hijo vacío.

**Eliminar:** localizar la clave. Si tiene subárbol derecho, reemplazarla por su
sucesor; si solo tiene izquierdo, usar su predecesor. Luego eliminar la clave
de reemplazo en ese subárbol. Si ambos hijos adyacentes están vacíos, quitar la
clave y ajustar las posiciones de hijos. Un nodo sin claves se elimina.

**BFS:** utilizar una cola; visitar un nodo y agregar sus hijos de izquierda a
derecha. Se aprovecha también para altura, amplitud y conteos.

Los recorridos se generalizan por clave, para un nodo con claves `K0...Kk-1`
e hijos `H0...Hk`:

- Inorden: `H0, K0, H1, K1, ..., Hk-1, Kk-1, Hk`.
- Preorden: `K0, H0, K1, H1, ..., Kk-1, Hk-1, Hk`.
- Postorden: `H0, H1, K0, H2, K1, ..., Hk, Kk-1`.

Cada `H` representa recorrer recursivamente ese subárbol. Con orden 2 se
obtienen los recorridos habituales del ABB.

## Ejemplo verificable

Orden 3, inserciones: `30, 50, 10, 20, 40, 60, 70`.

| Consulta | Resultado |
| --- | --- |
| Raíz | `[30, 50]` |
| BFS | `[[30, 50], [10, 20], [40], [60, 70]]` |
| Inorden | `[10, 20, 30, 40, 50, 60, 70]` |
| Preorden | `[30, 10, 20, 50, 40, 60, 70]` |
| Postorden | `[10, 20, 40, 30, 60, 70, 50]` |
| Nodos / claves / hojas | `4 / 7 / 3` |
| Altura / amplitud | `1 / 3` |

## Complejidad y alcance

Con `h` como altura y `m` como orden, búsqueda, inserción y eliminación requieren
como máximo `O(m · (h + 1))` trabajo en esta implementación. No se garantiza
altura logarítmica: un árbol M-vías sin balanceo puede crecer en una cadena.
Los recorridos y conteos visitan todos los nodos y sus posiciones de hijos:
`O(m · N)`, con `N` nodos físicos. Para orden fijo equivale a `O(N)`.

Los recorridos DFS, la eliminación y la verificación de balance usan recursión;
un árbol degenerado muy profundo puede alcanzar el límite de recursión de Python.
Las pruebas incluyen órdenes 2, 3, 4 y 6, eliminaciones de claves internas,
árbol vacío, duplicados y secuencias mezcladas comparadas con un conjunto.
