"""Convierte los nodos del modelo en posiciones para dibujarlos en SVG."""


def representar(arbol):
    """Ubica los nodos por inorden y profundidad, sin alterar el árbol."""
    nodos = []
    enlaces = []

    def visitar(nodo, nivel):
        if nodo is None:
            return
        visitar(nodo.get_izquierdo(), nivel + 1)
        nodos.append({
            "valor": nodo.get_dato(),
            "x": 55 + len(nodos) * 86,
            "y": 65 + nivel * 90,
            "nivel": nivel,
            "hoja": arbol.EsHoja(nodo),
        })
        for hijo, lado in ((nodo.get_izquierdo(), "I"),
                           (nodo.get_derecho(), "D")):
            if hijo is not None:
                enlaces.append({
                    "desde": nodo.get_dato(),
                    "hasta": hijo.get_dato(), "lado": lado,
                })
        visitar(nodo.get_derecho(), nivel + 1)

    visitar(arbol.get_raiz(), 0)
    ancho = max(640, len(nodos) * 86 + 24)
    if nodos and len(nodos) * 86 + 24 < ancho:
        margen = (ancho - (len(nodos) * 86 + 24)) / 2
        for nodo in nodos:
            nodo["x"] += margen
    return {
        "nodos": nodos, "enlaces": enlaces, "ancho": ancho,
        "alto": max(320, (arbol.Altura() + 1) * 90 + 55),
    }
