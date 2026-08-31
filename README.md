# Estructura de Datos II: árboles binarios

Este repositorio reúne prácticas de árboles binarios implementadas en Python 3.
El trabajo anterior se mantiene en sus archivos originales y las prácticas
nuevas están separadas en su propia carpeta.

## 1. ADT Árbol Binario con Tres en Raya

La implementación original usa cada nodo para almacenar una matriz de `3 x 3`
que representa un estado del juego Tres en Raya.

La clase `Nodo`, definida en `nodo.py`, incluye:

- matriz de `3 x 3`;
- hijo izquierdo e hijo derecho;
- métodos de acceso y modificación;
- validación de la matriz;
- presentación del tablero en consola.

La clase `Arbol`, definida en `arbol.py`, incluye:

- acceso y modificación de la raíz;
- inserción de la raíz y de hijos;
- recorridos preorden, inorden y postorden;
- búsqueda de tableros;
- verificación de árbol vacío.

Para ejecutar la práctica anterior:

```bash
python main.py
```

## 2. Árbol binario estático y dinámico

La carpeta `tarea_arbol_binario_metodos` agrega la práctica **Árbol binario:
Implementación de métodos** sin reemplazar las clases anteriores.

Incluye:

- una versión estática basada en una lista de capacidad configurable;
- una versión dinámica basada en objetos `Nodo`;
- inserción por nivel, de izquierda a derecha;
- los métodos `InsertarNodo`, `EsVacio`, `EsHoja`, `BuscarX`, `InOrden`,
  `PostOrden` y `PreOrden`;
- ejemplos de uso y pruebas automatizadas.

## 3. Árbol de expresiones

La misma carpeta contiene una práctica adicional que valida una expresión
infija, la convierte a posfija mediante una pila y construye su árbol de
expresión. Admite operandos alfanuméricos simples, `+`, `-`, `*`, `/` y
paréntesis.

Ejemplo:

```text
Infija:  (A+B)*C
Posfija: AB+C*
```

Para ejecutar todos los ejemplos:

```bash
python tarea_arbol_binario_metodos/main.py "(A+B)*C"
```

Para ejecutar todas las pruebas:

```bash
python -m unittest discover -v
```

La explicación completa de las representaciones, métodos y comandos está en
[`tarea_arbol_binario_metodos/README.md`](tarea_arbol_binario_metodos/README.md).

## 4. ADT Árbol Binario de Búsqueda

La carpeta `tarea_adt_arbol_binario_busqueda` contiene una implementación
orientada a objetos de un Árbol Binario de Búsqueda, con inserción, búsqueda,
altura, cantidad, amplitud y recorridos. La documentación está en
[`tarea_adt_arbol_binario_busqueda/README.md`](tarea_adt_arbol_binario_busqueda/README.md).
