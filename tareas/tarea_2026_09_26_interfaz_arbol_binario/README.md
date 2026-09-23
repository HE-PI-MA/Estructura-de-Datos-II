# Interfaz gráfica de un árbol binario

**Materia:** Estructura de Datos II (INF310), UAGRM.  
**Cierre publicado:** 26/09/2026, 00:52.  
**Entrega:** archivo ZIP en la actividad «Tarea Unidad 1: Crear interfaz grafica».

Aplicación local con Flask, HTML, CSS, JavaScript y un diagrama SVG. Los botones
llaman a los métodos de la clase `ArbolBinarioBusqueda` en Python. JavaScript
presenta las respuestas y anima los recorridos calculados por el servidor.

## Iniciar desde el repositorio en Windows

Requiere Python 3.9 o posterior. En la terminal PowerShell de Visual Studio Code,
con la carpeta del repositorio abierta, ejecutar:

```powershell
py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r .\tareas\tarea_2026_09_26_interfaz_arbol_binario\requirements.txt
& .\.venv\Scripts\python.exe .\tareas\tarea_2026_09_26_interfaz_arbol_binario\app.py
```

Abrir **http://127.0.0.1:5000** en Chrome o Edge. Mantener la terminal abierta.
Para detener el servidor, pulsar `Ctrl+C`. No hace falta activar el entorno ni
cambiar la política de ejecución de PowerShell. Si el puerto está ocupado,
agregar `--port 5001` al último comando y abrir http://127.0.0.1:5001.

## Iniciar después de extraer el ZIP

Abrir en VS Code la carpeta que contiene `app.py`, `models`, `controllers`,
`templates` y `static`. En su terminal:

```powershell
py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe app.py
```

En Linux/Fedora se pueden usar `python3 -m venv .venv`,
`.venv/bin/python -m pip install -r requirements.txt` y
`.venv/bin/python app.py`. El ZIP contiene todos los módulos propios necesarios.

## Demostración para la clase

1. Pulsar **Cargar ejemplo**: se insertan 50, 30, 70, 20, 40, 60 y 80.
2. Comprobar 7 nodos, altura 2, 4 hojas y amplitud 4.
3. Buscar 40: se destacan los nodos 50 → 30 → 40.
4. Consultar si 20 es hoja; comprobar también la raíz, el mínimo y el máximo.
5. Elegir **Por niveles**: 50, 30, 70, 20, 40, 60, 80.
6. Probar **Paso siguiente** y **Reproducir**; comparar los otros recorridos.
7. Eliminar 20 (hoja), 30 (un hijo) y 50 (dos hijos). La nueva raíz es 60.
8. Insertar un valor nuevo y uno repetido: el repetido se omite.
9. Recargar la página para comprobar que se conserva el árbol de esta sesión.
10. Pulsar **Vaciar árbol** y confirmar para empezar de nuevo.

## Métodos y controles

| Método de Python | Uso en la interfaz |
| --- | --- |
| `Insertar`, `Buscar`, `Eliminar` | Formularios de operaciones |
| `EsHoja` | Botón «¿Este nodo es una hoja?» |
| `Cantidad`, `Altura`, `CantidadHojas`, `Amplitud` | Tarjetas de medidas |
| `Raiz`, `Minimo`, `Maximo` | Consultas rápidas |
| `InOrden`, `PreOrden`, `PostOrden`, `PorNiveles` | Recorridos y reproducción |
| `EstaVacio`, `EsBalanceado` | Estado del árbol |
| `Camino` | Nodos examinados durante una búsqueda |
| Getters y setters de `Nodo` y del árbol | Construcción, consulta y dibujo del modelo |

La altura se mide en aristas: árbol vacío = −1; una raíz sola = 0.
La amplitud es el máximo número de nodos de un nivel. El árbol es un ABB;
el indicador de balance compara alturas, pero **no realiza rotaciones AVL**.
Se admiten hasta 63 valores únicos, enteros de −9999 a 9999.

## Organización del código

| Archivo o carpeta | Responsabilidad |
| --- | --- |
| `app.py` | Crear y ejecutar Flask |
| `models/nodo.py` | Nodo y sus getters/setters |
| `models/arbol.py` | Algoritmos del ABB |
| `controllers/home_controller.py` | Validar entradas y ejecutar operaciones |
| `controllers/visualizacion.py` | Calcular posiciones del diagrama |
| `templates/index.html` | Estructura de la página |
| `static/estilos.css` | Presentación y adaptación al ancho de pantalla |
| `static/arbol.js` | Eventos, dibujo SVG y animación |
| `tests.py` | Pruebas de las operaciones web |

El árbol se guarda como preorden en una cookie de sesión firmada por Flask.
Cada navegador conserva su propia sesión. No hay base de datos: esta práctica
no ofrece almacenamiento permanente. Reiniciar el servidor genera otra clave
de sesión, salvo que se configure `ARBOL_SECRET_KEY` en el entorno.

## Pruebas y ZIP

Desde esta carpeta, con Flask instalado:

```powershell
& .\.venv\Scripts\python.exe -m unittest tests -v
```

Si el entorno está en la raíz del repositorio, ejecutar allí:

```powershell
& .\.venv\Scripts\python.exe -m unittest discover -v
py crear_zip.py --tarea interfaz
```

El ZIP se genera en `entregas/Tarea_Interfaz_Arbol_Binario_2026-09-26.zip`.
Las 16 pruebas de esta tarea verifican recorridos, eliminación en sus tres
casos, búsqueda, medidas, sesiones separadas, límites y entradas inválidas.

## Referencias utilizadas

- [envWeb del ingeniero](https://github.com/profjcp/envWeb): referencia de organización en modelos, controladores y plantillas.
- [Unidad 1 del curso](https://github.com/profjcp/INF310-EstructurasDatos2): algoritmos de árboles binarios de búsqueda.
- [ArbolBB.ipynb](https://colab.research.google.com/drive/1xN0O9kWTRkAabjSra7OZNv9YpBM2oDT4): ejemplo de inserción que omite duplicados.
- La clase ABB y Nodo de la tarea propia del 01/09 se reutilizan aquí con métodos adicionales para el visualizador.
- [Documentación de Flask](https://flask.palletsprojects.com/en/stable/).

La consigna indica una base en GitHub sin identificar su enlace exacto.
Se tomó `envWeb` como referencia de estructura; esta entrega implementa la
interfaz del ABB y puede ejecutarse por separado.
