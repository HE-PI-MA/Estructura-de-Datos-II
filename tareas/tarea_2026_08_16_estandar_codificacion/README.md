# Tarea sobre estándar de codificación

**Materia:** Estructura de Datos II, UAGRM.

**Cierre publicado:** 16/08/2026, 23:17.

**Consigna:** realizar la estructura de una clase Árbol Binario,
implementar todos sus getters y setters y aplicar PEP8. Entregar ZIP o RAR.

## Ejecutar en Visual Studio Code

Desde la raíz del repositorio, en PowerShell:

```powershell
py tareas/tarea_2026_08_16_estandar_codificacion/main.py
```

Si se descargó el ZIP, primero extraerlo y abrir la carpeta en VS Code.
Desde la carpeta que contiene `main.py`:

```powershell
py main.py
```

Solo requiere Python 3. No necesita Flask ni instalar dependencias.

## Archivos

| Archivo | Contenido |
| --- | --- |
| `nodo.py` | Clase `Nodo`: dato, hijo izquierdo e hijo derecho |
| `arbol_binario.py` | Clase `ArbolBinario`: referencia a la raíz |
| `main.py` | Demostración de todos los getters y setters |
| `__init__.py` | Identifica la carpeta como paquete de Python |

Cada nodo puede tener hasta dos hijos. Un hijo ausente se representa con
`None`; un árbol vacío tiene raíz `None`. Esta práctica construye la estructura
mediante setters. Los valores 50, 30 y 70 son datos de ejemplo; no existe una
inserción automática ni se exige un orden de búsqueda en esta consigna.

## Todos los getters y setters

Un **getter** permite consultar un atributo. Un **setter** permite cambiarlo.

| Clase | Atributo | Getter | Setter |
| --- | --- | --- | --- |
| `ArbolBinario` | `__raiz` | `get_raiz()` | `set_raiz(nodo)` |
| `Nodo` | `__dato` | `get_dato()` | `set_dato(dato)` |
| `Nodo` | `__izquierdo` | `get_izquierdo()` | `set_izquierdo(nodo)` |
| `Nodo` | `__derecho` | `get_derecho()` | `set_derecho(nodo)` |

Los setters de raíz e hijos aceptan objetos `Nodo` o `None`.
Si reciben otro tipo, generan `TypeError` antes de modificar el atributo.
El dato puede ser un número, texto u otro valor de Python.
Al enlazar nodos, el programador debe conservar una estructura de árbol:
un hijo no debe apuntar a sus antecesores ni pertenecer a dos padres.

## Estándares PEP8 aplicados

- Sangría de cuatro espacios, sin tabulaciones.
- Clases con nombres como `ArbolBinario` y `Nodo`.
- Métodos y variables en `snake_case`, por ejemplo `get_raiz`.
- Líneas de código de hasta 79 caracteres.
- Docstrings breves para explicar módulos, clases y métodos.
- Espacios alrededor de operadores y después de comas.
- Separación con líneas en blanco entre clases, funciones y métodos.
- Importaciones al inicio y ejecución protegida con `if __name__`.

Se usan getters y setters explícitos porque así lo pide el ejercicio.
Referencia: [guía oficial PEP 8](https://peps.python.org/pep-0008/).

## Salida de la demostración

```text
Árbol vacío: True

Árbol creado con setters:
Raíz: 50
Hijo izquierdo: 30
Hijo derecho: 70

Nuevo dato del hijo izquierdo: 25
Hijo derecho retirado: True
Hijo izquierdo retirado: True
Árbol vacío nuevamente: True
```

## Verificar el estilo y generar el ZIP

La revisión de estilo es opcional para ejecutar el programa:

```powershell
py -m pip install pycodestyle
py -m pycodestyle tareas/tarea_2026_08_16_estandar_codificacion
```

Si no aparecen mensajes, la herramienta no encontró infracciones de las
reglas que comprueba. También se revisaron los nombres y la documentación.

Desde la raíz del repositorio, generar la entrega:

```powershell
py crear_zip.py --tarea estandar
```

Resultado: `entregas/Tarea_Estandar_Codificacion_2026-08-16.zip`.
Subirlo sin descomprimir a «Tarea sobre estandar de condificación» en
Presencial. Preparar este ZIP no registra automáticamente un envío.
