"""Recibe acciones, consulta los modelos y devuelve el estado de la sesión."""
import hmac
import secrets
from flask import Blueprint, jsonify, render_template, request, session
from models.juego import jugar, resultado
from models.ia import elegir

rutas = Blueprint('partida', __name__)


def estado(**extras):
    tablero = session.get('tablero', [''] * 9)
    return {'tablero': tablero, 'resultado': resultado(tablero), **extras}


@rutas.get('/')
def inicio():
    session.setdefault('csrf', secrets.token_hex(24))
    session.setdefault('tablero', [''] * 9)
    return render_template('index.html', token=session['csrf'], datos=estado())


@rutas.before_request
def proteger():
    if request.method == 'POST':
        token = request.headers.get('X-CSRF-Token', '')
        if not token or not hmac.compare_digest(token, session.get('csrf', '')):
            return jsonify(error='Recarga la página para continuar.'), 403


@rutas.post('/jugar')
def movimiento():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict) or datos.get('algoritmo') not in ('minimax', 'alfa_beta'):
        return jsonify(error='Selecciona un algoritmo válido.'), 400
    try:
        tablero = jugar(session.get('tablero', [''] * 9), datos.get('casilla'), 'X')
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    analisis = None
    if not resultado(tablero):
        analisis = elegir(tablero, datos['algoritmo'] == 'alfa_beta')
        tablero = jugar(tablero, analisis['casilla'], 'O')
    session['tablero'] = tablero
    return jsonify(estado(analisis=analisis))


@rutas.post('/reiniciar')
def reiniciar():
    session['tablero'] = [''] * 9
    return jsonify(estado())


@rutas.post('/comparar')
def comparar():
    # Comparación de la decisión anterior de O: quitar su última jugada no
    # sería seguro. Usamos un caso fijo y visible para ambos algoritmos.
    tablero = ['X', '', '', '', '', '', '', '', '']
    return jsonify(minimax=elegir(tablero, False),
                   alfa_beta=elegir(tablero, True))
