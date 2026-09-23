"""Genera ZIP independientes de las tareas, sin archivos temporales."""
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

TAREAS = {
    'mvias': ('tarea_2026_09_23_mvias_metodos', 'Tarea_Mvias_Metodos_2026-09-23.zip'),
    'interfaz': ('tarea_2026_09_26_interfaz_arbol_binario', 'Tarea_Interfaz_Arbol_Binario_2026-09-26.zip'),
}
EXTENSIONES = {'.py', '.md', '.txt', '.html', '.css', '.js', '.svg'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tarea', choices=TAREAS, default='mvias')
    args = parser.parse_args()
    raiz = Path(__file__).resolve().parent
    carpeta, nombre_zip = TAREAS[args.tarea]
    tarea = raiz / 'tareas' / carpeta
    destino = raiz / 'entregas' / nombre_zip
    destino.parent.mkdir(exist_ok=True)
    with ZipFile(destino, 'w', ZIP_DEFLATED) as archivo:
        for ruta in sorted(tarea.rglob('*')):
            relativa = ruta.relative_to(tarea)
            if any(p.startswith('.') or p == '__pycache__' for p in relativa.parts):
                continue
            if ruta.is_file() and ruta.suffix in EXTENSIONES:
                archivo.write(ruta, relativa)
    print(f'ZIP creado: {destino}')


if __name__ == '__main__':
    main()
