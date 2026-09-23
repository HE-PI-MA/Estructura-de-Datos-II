"""Genera el ZIP independiente solicitado para la tarea M-vías."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    raiz = Path(__file__).resolve().parent
    tarea = raiz / "tareas" / "tarea_2026_09_23_mvias_metodos"
    destino = raiz / "entregas" / "Tarea_Mvias_Metodos_2026-09-23.zip"
    destino.parent.mkdir(exist_ok=True)
    with ZipFile(destino, "w", ZIP_DEFLATED) as archivo:
        for ruta in sorted(tarea.iterdir()):
            if ruta.is_file() and ruta.suffix in (".py", ".md"):
                archivo.write(ruta, ruta.name)
    print(f"ZIP creado: {destino}")


if __name__ == "__main__":
    main()
