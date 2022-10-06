import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input,Output

Columns = ("Depart ", "Arrivée ", "Heure de départ ", "Heure d'arrivée ", "Durée ")
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
    + [html.Div(id="out-all-types")]

)

@app.callback(
    Output("out-all-types", "children"),
    [Input("input_{}".format(i), "value") for i in range(5)],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))

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