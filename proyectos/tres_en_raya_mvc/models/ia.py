"""Minimax y poda alfa-beta sobre un árbol implícito de estados."""
from .juego import resultado


def elegir(tablero, poda=True):
    """O maximiza y X minimiza. Backtracking restaura cada jugada probada."""
    tablero = tablero.copy()
    estadisticas = {'estados': 0, 'cortes': 0}

    def evaluar(turno, profundidad, alfa, beta):
        estadisticas['estados'] += 1
        fin = resultado(tablero)
        if fin:
            return 10 - profundidad if fin == 'O' else (
                profundidad - 10 if fin == 'X' else 0)
        mejor = -100 if turno == 'O' else 100
        for i in range(9):
            if tablero[i]:
                continue
            tablero[i] = turno
            try:
                valor = evaluar('X' if turno == 'O' else 'O',
                                profundidad + 1, alfa, beta)
            finally:
                tablero[i] = ''
            if turno == 'O':
                mejor = max(mejor, valor)
                alfa = max(alfa, mejor)
            else:
                mejor = min(mejor, valor)
                beta = min(beta, mejor)
            if poda and alfa >= beta:
                estadisticas['cortes'] += 1
                break
        return mejor

    if resultado(tablero):
        return {'casilla': None, 'valor': 0, **estadisticas}
    mejor, casilla, alfa = -100, None, -100
    for i in range(9):
        if tablero[i]:
            continue
        tablero[i] = 'O'
        try:
            valor = evaluar('X', 1, alfa, 100)
        finally:
            tablero[i] = ''
        if valor > mejor:
            mejor, casilla = valor, i
        alfa = max(alfa, mejor)
    return {'casilla': casilla, 'valor': mejor, **estadisticas}
