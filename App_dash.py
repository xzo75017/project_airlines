import dash
from dash.dependencies import Input,Output
from Dash_Handler import dash_handler
from dash import dash_table, dcc, html
import pandas as pd

Columns = ("Depart ", "Arrivée ", "Heure de départ ", "Heure d'arrivée ", "Durée ")

df = pd.DataFrame(columns = ["id_vol","departureTime","arrivalTime","duration","departureAirportCode","arrivalAirportCode","airlineCodes","departureDate", "arrivalDate"])
ALLOWED_TYPES = (
    "text"
)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
        html.P(Columns)]
        
        + [dcc.Input(
            id="input_{}".format(i),
            type="text",
            placeholder="input type {}".format(i),
        )
        for i in range (5)
    ]
        + [html.Div(id = "Vol")]

)

@app.callback(
    Output("Vol", "children"),
    [Input("input_{}".format(i), "value") for i in range(5)],
)
def cb_render(*vals):
    result = dash_handler(vals)
    df1 = pd.DataFrame(result)
    return [
       dash_table.DataTable(
            df1.to_dict('records'),
            [{"name": i, "id": i} for i in df1.columns]
            
       ) 
    ]

        
    #return id, HD, HA, Dur, Arp_dep, Arp_arr, Air, Dep, Arr
        

# @app.callback(Output(component_id='graph_1', component_property='figure'),
#             [Input(component_id='Dropdown', component_property='value'),
#              Input(component_id = 'slider_1', component_property='value')])
# def update_graph(indicator, slider):
#     # Création de la figure plotly
#     df_1 = df[df["year"] == slider]
#     fig = px.scatter(df_1, x="gdpPercap",
#                         y=indicator,
#                         color="continent",
#                         hover_name="country")
#     return fig




if __name__=="__main__":
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)