"""Recibe acciones web y llama a los métodos de la clase árbol."""

import re
import secrets

from flask import Blueprint, jsonify, render_template, request, session

from .visualizacion import representar

if __package__.startswith("tareas."):
    from ..models.arbol import ArbolBinarioBusqueda
else:
    from models.arbol import ArbolBinarioBusqueda

web = Blueprint("web", __name__)
MAX_NODOS = 63
MAX_VALOR = 9999
EJEMPLO = [50, 30, 70, 20, 40, 60, 80]


def recuperar_arbol():
    """Reconstruye la forma exacta usando el preorden de la sesión."""
    arbol = ArbolBinarioBusqueda()
    for valor in session.get("preorden", []):
        arbol.Insertar(valor)
    return arbol


def estado(arbol):
    """Consulta los métodos del modelo para presentar sus resultados."""
    return {
        "grafico": representar(arbol),
        "resumen": {
            "cantidad": arbol.Cantidad(), "altura": arbol.Altura(),
            "hojas": arbol.CantidadHojas(), "amplitud": arbol.Amplitud(),
            "raiz": arbol.Raiz(), "minimo": arbol.Minimo(),
            "maximo": arbol.Maximo(), "vacio": arbol.EstaVacio(),
            "balanceado": arbol.EsBalanceado(),
        },
        "recorridos": {
            "inorden": arbol.InOrden(), "preorden": arbol.PreOrden(),
            "postorden": arbol.PostOrden(), "niveles": arbol.PorNiveles(),
        },
        "csrf": session.setdefault("csrf", secrets.token_urlsafe(24)),
    }


def validar_entero(valor):
    if type(valor) is not int or abs(valor) > MAX_VALOR:
        raise ValueError("Usa números enteros entre -9999 y 9999.")
    return valor


def leer_valores(entrada):
    """Valida toda la entrada antes de modificar el árbol."""
    if not isinstance(entrada, str) or not entrada.strip():
        raise ValueError("Escribe al menos un número entero.")
    partes = re.split(r"[,;\s]+", entrada.strip())
    if len(partes) > MAX_NODOS:
        raise ValueError("Puedes ingresar hasta 63 valores por operación.")
    valores = []
    for parte in partes:
        if not re.fullmatch(r"[+-]?[0-9]{1,4}", parte):
            raise ValueError("Separa los enteros con comas o espacios.")
        valores.append(validar_entero(int(parte)))
    return valores


@web.get("/")
def index():
    return render_template("index.html", inicial=estado(recuperar_arbol()))


@web.get("/api/arbol")
def consultar():
    return jsonify(estado(recuperar_arbol()))


@web.post("/api/operar")
def operar():
    token = request.headers.get("X-CSRF-Token", "")
    if not token or not secrets.compare_digest(token, session.get("csrf", "")):
        return jsonify(error="Recarga la página para continuar."), 403
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify(error="La solicitud debe contener una operación."), 400
    arbol = recuperar_arbol()
    accion = datos.get("accion")
    camino = []
    destacado = None
    encontrado = None
    try:
        if accion == "insertar":
            valores = leer_valores(datos.get("valores"))
            if len(set(arbol.InOrden()) | set(valores)) > MAX_NODOS:
                raise ValueError("El visualizador admite hasta 63 nodos.")
            nuevos = [v for v in valores if arbol.Insertar(v)]
            omitidos = len(valores) - len(nuevos)
            mensaje = f"Se agregaron {len(nuevos)} valores."
            if omitidos:
                mensaje += f" Se omitieron {omitidos} duplicados."
            if nuevos:
                destacado = nuevos[-1]
                camino = arbol.Camino(destacado)
        elif accion in ("buscar", "eliminar", "es_hoja"):
            valor = validar_entero(datos.get("valor"))
            camino = arbol.Camino(valor)
            nodo = arbol.Buscar(valor)
            encontrado = nodo is not None
            if not encontrado:
                mensaje = f"El valor {valor} no está en el árbol."
            elif accion == "eliminar":
                arbol.Eliminar(valor)
                camino = []
                mensaje = f"Se eliminó {valor}."
            else:
                destacado = valor
                if accion == "es_hoja":
                    es_hoja = arbol.EsHoja(nodo)
                    mensaje = (f"{valor} es una hoja: no tiene hijos." if es_hoja
                               else f"{valor} no es una hoja: tiene hijos.")
                else:
                    mensaje = f"Encontrado: {valor}."
        elif accion == "ejemplo":
            arbol = ArbolBinarioBusqueda()
            for valor in EJEMPLO:
                arbol.Insertar(valor)
            mensaje = "Ejemplo cargado: 50, 30, 70, 20, 40, 60, 80."
        elif accion == "vaciar":
            arbol.set_raiz(None)
            mensaje = "Árbol vacío. Puedes comenzar de nuevo."
        elif accion in ("minimo", "maximo", "raiz"):
            metodo = {"minimo": arbol.Minimo, "maximo": arbol.Maximo,
                      "raiz": arbol.Raiz}[accion]
            destacado = metodo()
            if destacado is None:
                mensaje = "El árbol está vacío. Inserta un valor primero."
            else:
                camino = arbol.Camino(destacado)
                etiqueta = {"minimo": "Mínimo", "maximo": "Máximo",
                            "raiz": "Raíz"}[accion]
                mensaje = f"{etiqueta}: {destacado}."
        else:
            raise ValueError("Elige una operación válida.")
    except ValueError as error:
        return jsonify(error=str(error)), 400
    # Guardar preorden después de eliminar conserva la nueva raíz y los hijos.
    session["preorden"] = arbol.PreOrden()
    resultado = estado(arbol)
    resultado.update(mensaje=mensaje, camino=camino, destacado=destacado,
                     encontrado=encontrado)
    return jsonify(resultado)
