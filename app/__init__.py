from dash import Dash
from dash_core_components import Graph
from dash_html_components import Div
from flask import Flask
from pendulum import datetime

from app.graphs.burn_down import burn_down


def create_app():
    app = Flask(__name__)
    dash_app = Dash(__name__, server=app)

    dash_app.layout = Div(
        children=[
            Graph(
                config={'displayModeBar': False},
                figure=burn_down(
                    sprint='',
                    initial_data=datetime(2021, 4, 5),
                    final_data=datetime(2021, 4, 16),
                    total_points=50,
                    sprint_data=[50, 45, 41, 37, 39, 12],
                ),
            )
        ]
    )

    @app.route('/')
    def index():
        return dash_app.index()

    return app
