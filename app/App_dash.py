from dash import Dash, html, callback_context
from dash.dependencies import Input,Output, State
from Dash_utils import dash_event, creation_dash_table, date_range, city_to_code, data_handler_vol
import Dash_components as dc
import dash_bootstrap_components as dbc
from datetime import datetime as dt

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([dc.Vol, dc.sidebar])

@app.callback(
    Output('Tableau', 'children'),
    Input('submit-val', 'n_clicks'),
    State('my-date-picker-range', 'start_date'),
    State('my-date-picker-range', 'end_date'),
    State('ville_event', 'value'),
    State('ville_dep', 'value'),
    State('passagers0', 'value'),
    State('passagers1', 'value'),
    State('passagers2', 'value'),
)
def date_event(btn_event, start_date, end_date, arrivee, depart, adulte, enfant, bebe):
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
    else :
        return "Selectionnez des dates"

@app.callback(
    Output('Vol', 'children'),
    Input('submit-val2', 'n_clicks'),
    State('my-date-picker-range', 'start_date'),
    State('my-date-picker-range', 'end_date'),
    State('ville_event', 'value'),
    State('ville_dep', 'value'),
    State('passagers0', 'value'),
    State('passagers1', 'value'),
    State('passagers2', 'value'),
)
def recherche_vol(btn_vol, start_date, end_date, arrivee, depart, adulte, enfant, bebe):
    if start_date is not None and end_date is not None and arrivee is not None and depart is not None and adulte is not None and enfant is not None and bebe is not None:
        print('Ville de départ : ', depart)
        ville_dep =  city_to_code(depart)
        print("Code de ville de départ : ", ville_dep)
        ville_arr = city_to_code(arrivee)
        print("Code de ville d'arrivée : ", ville_arr)
        result = data_handler_vol(depart, arrivee, ville_dep, ville_arr, start_date, adulte, enfant, bebe)
        return creation_dash_table(result)       
    else:
        return "Complétez les informations"


if __name__=="__main__":
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)