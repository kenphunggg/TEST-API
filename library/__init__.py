from flask import Flask, request, Blueprint
from .books.controller import books
# from .extension import ma

def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    # Load file config
    app.config.from_pyfile(config_file)
    # Load blueprint api books
    app.register_blueprint(books)
    return app