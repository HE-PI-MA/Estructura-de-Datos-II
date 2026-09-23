"""Reglas del juego; no depende de Flask ni de la interfaz."""
LINEAS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
          (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def resultado(tablero):
    for a, b, c in LINEAS:
        if tablero[a] and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    return 'empate' if all(tablero) else None


def jugar(tablero, casilla, ficha):
    if type(casilla) is not int or not 0 <= casilla < 9:
        raise ValueError('Selecciona una casilla del tablero.')
    if resultado(tablero):
        raise ValueError('La partida terminó. Inicia otra partida.')
    if tablero[casilla]:
        raise ValueError('Esa casilla está ocupada.')
    nuevo = tablero.copy()
    nuevo[casilla] = ficha
    return nuevo
