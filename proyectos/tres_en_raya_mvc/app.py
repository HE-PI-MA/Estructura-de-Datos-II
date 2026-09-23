"""Entrada local de la aplicación Flask MVC."""
import os
import secrets
from flask import Flask
from controllers.partida import rutas


def crear_app():
    app = Flask(__name__)
    app.config.update(SECRET_KEY=os.environ.get('SECRET_KEY') or secrets.token_hex(32),
                      MAX_CONTENT_LENGTH=4096, SESSION_COOKIE_HTTPONLY=True,
                      SESSION_COOKIE_SAMESITE='Lax')
    app.register_blueprint(rutas)
    return app


if __name__ == '__main__':
    crear_app().run(host='127.0.0.1', port=5001, debug=False)
