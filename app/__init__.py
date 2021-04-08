from flask import Flask
from dash import Dash


def create_app():
    app = Flask(__name__)
    dash_app = Dash(__name__, server=app)

    return app
