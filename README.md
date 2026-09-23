# Estructura de Datos II

Prácticas en Python de la materia INF310, grupo SA, UAGRM, semestre 2-2026.
Docente: Ing. Juan Carlos Peinado Pereira.

Cada tarea tiene su carpeta dentro de `tareas/`, con fecha de cierre y un nombre
descriptivo. Este índice presenta primero la tarea más antigua.
Las fechas se consultaron en Presencial el 23 de septiembre de 2026.

## Tareas con código

| Cierre | Tarea | Carpeta |
| --- | --- | --- |
| 16/08/2026, 23:17 | Árbol binario: getters, setters y PEP8 | [Estándar de codificación](tareas/tarea_2026_08_16_estandar_codificacion/) |
| 20/08/2026, 07:00 | ADT árbol binario: Tres en Raya | [ADT árbol binario](tareas/tarea_2026_08_20_adt_arbol_binario/) |
| 01/09/2026, 07:00 | Métodos del árbol binario y árbol de expresiones | [Métodos y expresiones](tareas/tarea_2026_09_01_metodos_y_expresiones/) |
| 01/09/2026, 23:17 | Representación del ADT árbol binario de búsqueda | [ABB](tareas/tarea_2026_09_01_abb/) |
| 06/09/2026, 23:17 | Investigación e implementación AVL | [AVL](tareas/tarea_2026_09_06_avl/) |
| 23/09/2026, 23:17 | M-vías: métodos del ABB | [M-vías](tareas/tarea_2026_09_23_mvias_metodos/) |
| 26/09/2026, 00:52 | Interfaz gráfica del árbol binario | [Interfaz Flask](tareas/tarea_2026_09_26_interfaz_arbol_binario/) |

El [cronograma completo](CRONOGRAMA.md) conserva los nombres de las 22 tareas,
sus fechas y enlaces a Presencial. Tener código en GitHub no registra una entrega
en la plataforma: cada actividad se presenta en su enlace correspondiente.

## Trabajar en Visual Studio Code

Abrir la carpeta completa del repositorio en Visual Studio Code y usar su
terminal. El código de consola utiliza solamente la biblioteca estándar de
Python 3. No requiere instalar paquetes. La interfaz web sí necesita Flask; sus pasos aparecen abajo.

### Interfaz web en PowerShell

```powershell
py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r .\tareas\tarea_2026_09_26_interfaz_arbol_binario\requirements.txt
& .\.venv\Scripts\python.exe .\tareas\tarea_2026_09_26_interfaz_arbol_binario\app.py
```

Abrir http://127.0.0.1:5000 en el navegador. Para detener, `Ctrl+C`.
[Explicación y demostración de la interfaz](tareas/tarea_2026_09_26_interfaz_arbol_binario/README.md).

### Prácticas de consola

Ejecutar M-vías:

```bash
python tareas/tarea_2026_09_23_mvias_metodos/main.py
```

Abrir su menú para insertar, buscar y eliminar claves:

```bash
python tareas/tarea_2026_09_23_mvias_metodos/main.py --menu --orden 4
```

Ejecutar las prácticas anteriores:

```bash
python tareas/tarea_2026_09_06_avl/main.py
python tareas/tarea_2026_09_01_abb/main.py
python tareas/tarea_2026_09_01_metodos_y_expresiones/main.py "(A+B)*C"
python tareas/tarea_2026_08_20_adt_arbol_binario/main.py
```

En Windows puede usarse `py` en lugar de `python`.

## Comprobar el código

Desde la raíz del repositorio:

```bash
python -m pip install -r tareas/tarea_2026_09_26_interfaz_arbol_binario/requirements.txt
python -m unittest discover -v
```

Incluye 75 pruebas: ABB, métodos y expresiones, AVL, M-vías e interfaz web.
Usar el intérprete del entorno virtual cuando se hayan instalado allí los paquetes.
La práctica inicial de Tres en Raya conserva su demostración en `main.py`.

## Preparar los ZIP

```bash
python crear_zip.py --tarea estandar
python crear_zip.py --tarea mvias
python crear_zip.py --tarea interfaz
```

La entrega de estándares se genera en
`entregas/Tarea_Estandar_Codificacion_2026-08-16.zip`.

Se generan `entregas/Tarea_Interfaz_Arbol_Binario_2026-09-26.zip` y
`entregas/Tarea_Mvias_Metodos_2026-09-23.zip` con el código, las pruebas
y la explicación. El ZIP de M-vías se puede extraer en una carpeta aparte y ejecutar
con `python main.py`; las pruebas se ejecutan con `python -m unittest tests -v`.

## Organización anterior y nueva

| Antes | Ahora |
| --- | --- |
| `arbol.py`, `nodo.py`, `main.py` en la raíz | `tareas/tarea_2026_08_20_adt_arbol_binario/` |
| `tarea_arbol_binario_metodos/` | `tareas/tarea_2026_09_01_metodos_y_expresiones/` |
| `tarea_adt_arbol_binario_busqueda/` | `tareas/tarea_2026_09_01_abb/` |
| `tarea_arbol_avl/` | `tareas/tarea_2026_09_06_avl/` |

La fecha usa el formato año, mes y día. Los nombres no tienen espacios ni tildes
para facilitar los comandos de Python. Las carpetas se ordenan por su nombre;
el índice se mantiene de la más antigua a la más reciente.

## Referencias

- [Índice del Drive del ingeniero por temas](MATERIAL_DEL_INGENIERO.md).

- [Curso en Presencial](https://presencial.uagrm.edu.bo/course/view.php?id=135285).
- [Material del ingeniero](https://github.com/profjcp/INF310-EstructurasDatos2).
- [Base original del ADT](https://github.com/profjcp/adtcode).

## Proyecto de juego con MVC

[Tres en raya con Minimax y poda alfa-beta](proyectos/tres_en_raya_mvc/):
Flask, HTML, CSS y JavaScript; jugador contra computadora, comparación de
estados explorados y pruebas. Proyecto de avance, sin fecha de entrega confirmada.
