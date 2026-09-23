"""Aplicación Flask basada en la organización de profjcp/envWeb."""

import os
import secrets

from flask import Flask, jsonify

if __package__:
    from .controllers.home_controller import web
else:
    from controllers.home_controller import web


def create_app(config=None):
    """Crea una aplicación independiente para ejecutarla o probarla."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("ARBOL_SECRET_KEY") or secrets.token_hex(32),
        MAX_CONTENT_LENGTH=8192,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )
    if config:
        app.config.update(config)
    app.register_blueprint(web)

    @app.errorhandler(413)
    def entrada_grande(_error):
        return jsonify(error="La entrada es demasiado grande."), 413

    @app.after_request
    def evitar_cache(response):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    return app


app = create_app()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Interfaz del árbol binario")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()
    app.run(host="127.0.0.1", port=args.port, debug=False)
