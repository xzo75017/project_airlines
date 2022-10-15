from dash import Dash, html
from dash.dependencies import Input,Output, State
from Dash_utils import dash_vol, dash_event, creation_dash_table, date_range
import Dash_components as dc
import dash_bootstrap_components as dbc
from datetime import datetime as dt


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([dc.Event, dc.sidebar])


@app.callback(
    Output("Vol", "children"),
    [Input("input"+str(i), "value") for i in range(len(dc.Columns))],
)
def cb_render(*vals):
    '''
    Fonction callback permettant d'afficher tout le tableau d'association du SQL
    '''
    result = dash_vol(vals)
    return creation_dash_table(result)

@app.callback(
    Output('tableau-event', 'children'),
    Input('submit-val', 'n_clicks'),
    State('my-date-picker-range', 'start_date'),
    State('my-date-picker-range', 'end_date'),
    State('input1', 'value'))
def date_event(n_clicks, start_date, end_date, value):
    '''
    Fonction callback permettant d'afficher les evenements par rapport à la ville d'arrivée et aux Dates entrés dans les champs
    Paramètres :
    -n_clicks : nombre de cliques sur le bouton
    -start_date : date de départ
    -end_date : date de fin
    -value : valeur du champ de la ville d'arrivée
    '''
    if start_date is not None and end_date is not None:
        start_date_object = dt.fromisoformat(start_date)
        end_date_object = dt.fromisoformat(end_date)
        liste_dates = date_range(start_date_object, end_date_object)
        date = []
        for element in liste_dates:
            format = element.strftime('%b %d')
            split = format.split()
            date.append((split[0],split[1], value))
            print(date)
        result = dash_event(date)
            
        return creation_dash_table(result)
    else :
        return "Selectionnez des dates"
        



if __name__=="__main__":
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)