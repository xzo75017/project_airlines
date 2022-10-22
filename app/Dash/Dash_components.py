from dash import dcc, html
from . import Dash_css as css
from datetime import datetime as dt, timedelta as td

Columns = ("Départ",        #Champs de textes de la sidebar
        "Arrivée")

Columns_vol = ("Nombre d'adultes", "Nombre d'enfants", "Nombre de bébés")


Event = html.Div([html.H3(id = 'titre')] +  [dcc.Loading(id = "Event")], style =css.TABLE_STYLE)      #Tableau d'evenements)

Vol_aller = html.Div([html.H3(id = 'aller')] +  [dcc.Loading(id = "Vol_aller")], style =css.TABLE_STYLE)      #Tableau de vols_aller

Vol_retour = html.Div([html.H3(id = 'retour')] +  [dcc.Loading(id = "Vol_retour")], style =css.TABLE_STYLE)

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
    [html.P("Informations pour les evenements : "),
    html.Br(),
    dcc.Input(
                id = "ville_event",
                type="text",
                placeholder="Ville"
            )
    ]
    + [date] + 
    [html.Br(),
     html.Button('Trouver des evenements', id='submit-val', n_clicks=0)]
    +
    [
    html.Br(),
    html.Br(),
    html.P("Informations complémentaires pour les vols : "),
    dcc.Input(
                id = "ville_dep",
                type="text",
                placeholder="Ville de départ"
            )
    ]
    +
    [
    dcc.Input(
                id = "passagers"+str(i),
                type="number",
                placeholder=Columns_vol[i]
            )
            for i in range (len(Columns_vol))
    ]
    +
    [html.Br(),
     html.Br(),
     html.Button('Trouver des vols', id='submit-val2', n_clicks=0)]
)



sidebar = html.Div(                                         #Sidebar en elle-meme (titre, position, ce qu'elle contient)
    [
        html.H2('Project DST'),
        html.Hr(),
        table
    ],
    style = css.SIDEBAR_STYLE
)