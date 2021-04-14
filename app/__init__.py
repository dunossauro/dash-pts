from dash import Dash
from dash_core_components import Graph, Dropdown
from dash_html_components import Div, P, H1
from dash.dependencies import Input, Output
from flask import Flask
from pendulum import datetime

from app.graphs.burn_down import burn_down
from app.graphs.velocity import velocity


def create_app():
    app = Flask(__name__)

    dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')

    dash_app.layout = Div(
        children=[
            Div(
                children=[
                    P(children='📈', className='header-emoji'),
                    H1(children='Dash-PTS', className='header-title'),
                    P(
                        children='A free and Open Source PTS tool:',
                        className='header-description',
                    ),
                    P(
                        children='https://github.com/dunossauro/dash-pts',
                        className='header-description',
                    ),
                ],
                className='header'
            ),
            Div(
                children=[
                    Div(
                        children=[
                            Div(children='Department', className='menu-title'),
                            Dropdown(
                                id='department-name',
                                options=[
                                    {'label': i, 'value': i} for i in 'abcd'
                                ],
                                value='a',
                                className='dropdown'
                            )
                        ],
                    ),
                    Div(
                        children=[
                            Div(children='Team', className='menu-title'),
                            Dropdown(
                                id='team-name',
                                options=[
                                    {'label': i, 'value': i} for i in 'abcd'
                                ],
                                value='a',
                                className='dropdown'
                            )
                        ],
                    ),
                ],
                className='menu',
            ),
            Div(
                children=[
                    Graph(
                        id='burn-down',
                        className='card',
                        config={'displayModeBar': False},
                    ),
                    Graph(
                        id='velocity',
                        className='card',
                        config={'displayModeBar': False},
                    )
                ],
                className='wrapper',
            )
        ],
    )

    @app.route('/dash')
    def index():
        return dash_app.index()

    @dash_app.callback(
        [
            Output(component_id='burn-down', component_property='figure'),
            Output(component_id='velocity', component_property='figure'),
        ],
        [
            Input(component_id='team-name', component_property='value'),
            Input(component_id='department-name', component_property='value'),
        ]
    )
    def generate_graphs(team_name, department_name):
        return (
            burn_down(
                sprint='',
                initial_data=datetime(2021, 4, 5),
                final_data=datetime(2021, 4, 16),
                total_points=50,
                sprint_data=[50, 45, 41, 37, 39, 12],
            ),
            velocity({
                'names': ['Sprint ' + str(x) for x in range(1, 7)],
                'commitment': list(range(1, 7)),
                'completed': list(range(7, 15)),
            })
        )

    return app
