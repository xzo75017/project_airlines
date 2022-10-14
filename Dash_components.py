from dash import dcc, html
import dash_bootstrap_components as dbc 
import pandas as pd
import Dash_css as css
from datetime import datetime as dt, timedelta as td

Columns = ("Départ",        #Champs de textes de la sidebar
        "Arrivée")


Vol = html.Div([html.Div(id = "Vol")], style =css.TABLE_STYLE)      #Tableau d'association

Event = html.Div([html.Div(id = "tableau-event")], style =css.TABLE_STYLE)      #Tableau d'evenement

date = html.Div([                                         #Date de la sidebar
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt.now(),
        max_date_allowed=dt.now() + td(weeks=52),
        initial_visible_month=dt.now()
    ),
    html.Div(id='output-container-date-picker-range')
])

table = html.Div(                                         #Contenue de la sidebar (champs, bouton, date)
    [dcc.Input(
                id = "input"+str(i),
                type="text",
                placeholder=str(Columns[i])
            )
            for i in range (len(Columns))
    ]
    + [date] + 
    [html.Br(),
     html.Button('Submit', id='submit-val', n_clicks=0)]
)


sidebar = html.Div(                                         #Sidebar en elle-meme (titre, position, ce qu'elle contient)
    [
        html.H2('Parameters'),
        html.Hr(),
        table
    ],
    style = css.SIDEBAR_STYLE
)