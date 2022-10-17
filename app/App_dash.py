from dash import Dash, html, callback_context
from dash.dependencies import Input,Output, State
from Dash_utils import dash_vol, dash_event, creation_dash_table, date_range
import Dash_components as dc
import dash_bootstrap_components as dbc
from datetime import datetime as dt

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([dc.Tableau, dc.sidebar])

@app.callback(
    Output('Tableau', 'children'),
    Input('submit-val', 'n_clicks'),
    Input('submit-val2', 'n_clicks'),
    State('my-date-picker-range', 'start_date'),
    State('my-date-picker-range', 'end_date'),
    State('input0', 'value'),
    State('input1', 'value')
)
def date_event(btn_event, btn_vol, start_date, end_date, depart, arrivee):
    '''
    Fonction callback permettant d'afficher les evenements par rapport à la ville d'arrivée et aux Dates entrés dans les champs
    Paramètres :
    -n_clicks : nombre de cliques sur le bouton
    -start_date : date de départ
    -end_date : date de fin
    -value : valeur du champ de la ville d'arrivée
    '''
    if callback_context.triggered_id == 'submit-val':
        if start_date is not None and end_date is not None:
            start_date_object = dt.fromisoformat(start_date)
            end_date_object = dt.fromisoformat(end_date)
            liste_dates = date_range(start_date_object, end_date_object)
            date = []
            for element in liste_dates:
                format = element.strftime('%b %d')
                split = format.split()
                date.append((split[0],split[1], arrivee))
                print(date)
            result = dash_event(date)
            return creation_dash_table(result)
    elif callback_context.triggered_id == 'submit-val2':
        result = dash_vol(depart)
        return creation_dash_table(result)
    else :
        return "Selectionnez des dates"




if __name__=="__main__":
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)