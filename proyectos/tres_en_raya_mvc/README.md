# Tres en raya con MVC y búsqueda de jugadas

Avance de proyecto de Estructura de Datos II. La fecha y la actividad de entrega
están pendientes de confirmación del docente; no se identifica como examen.

## Ejecutar desde la raíz del repositorio en PowerShell

```powershell
py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r .\proyectos\tres_en_raya_mvc\requirements.txt
& .\.venv\Scripts\python.exe .\proyectos\tres_en_raya_mvc\app.py
```

Abrir http://127.0.0.1:5001. Detener con Ctrl+C. También se puede extraer el
ZIP y ejecutar `py -m pip install -r requirements.txt` y `py app.py` dentro
 de la carpeta extraída. Requiere Python 3.9 o posterior.

## MVC

- Modelo: models/juego.py contiene reglas; models/ia.py, búsqueda de jugadas.
- Vista: templates/index.html y static/ contienen interfaz y comunicación.
- Controlador: controllers/partida.py valida acciones y consulta los modelos.
- app.py crea la aplicación y registra el controlador.

X (persona) empieza; O (computadora) responde. Se detectan las ocho líneas
 ganadoras y el empate. No se puede jugar en una casilla ocupada ni después
 del final. Nueva partida vacía el tablero. Cada navegador guarda su partida
 en una sesión firmada; no hay base de datos. Reiniciar el servidor invalida
 las sesiones salvo que se configure una SECRET_KEY estable.

## Algoritmos para explicar en clase

Minimax asigna valores positivos a victorias de O y negativos a victorias
 de X, con 0 para empate. La profundidad favorece ganar antes o perder más
 tarde. O maximiza y X minimiza. En empates de valor se elige la primera
 casilla en orden de lectura. No se usa azar ni un servicio de IA externo.

Backtracking coloca una ficha provisional, explora y deshace esa ficha.
La poda alfa-beta conserva el resultado de Minimax evitando explorar ramas
 que ya no pueden mejorar la decisión. El selector permite usar ambos modos.

El árbol de estados es implícito: cada llamada recursiva representa un tablero;
 sus hijos son movimientos legales. Puede tener hasta nueve hijos inicialmente,
 no es un ABB ni un árbol AVL. No se almacena ni se dibuja el árbol completo.

El contador de estados mide llamadas a la evaluación, incluidos terminales;
 los cortes cuentan interrupciones del bucle por alfa >= beta, no el número
 de nodos omitidos. La comparación usa el mismo caso fijo (X en esquina),
 mientras los indicadores de la partida describen la última respuesta de O.

## Pruebas

Desde esta carpeta: `py -m unittest -v tests`.
La aplicación es para demostración local, sin despliegue público configurado.
