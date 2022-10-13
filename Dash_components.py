from dash import dcc, html
import dash_bootstrap_components as dbc 
import pandas as pd
import Dash_css as css

Columns = ("Départ",
        "Date de départ",
        "Arrivée",
        "Date d'arrivée")

df = pd.DataFrame(columns = ["id_vol","Heure de départ","Heure d'arrivée","Durée","Code d'aéroport de départ","Code d'aéroport d'arrivée'"
                             ,"Code airline","Date de départ", "Date d'arrivée"])
ALLOWED_TYPES = (
    "text"
)

Vol = html.Div([html.Div(id = "Vol")], style =css.TABLE_STYLE)

Event = html.Div([html.Div(id = "Event")], style =css.TABLE_STYLE)

table = html.Div(
    [dcc.Input(
                id = "input"+str(i),
                type="text",
                placeholder=str(Columns[i])
            )
            for i in range (len(Columns))
    ]
)

sidebar = html.Div(
    [
        html.H2('Parameters'),
        html.Hr(),
        table
    ],
    style = css.SIDEBAR_STYLE
)