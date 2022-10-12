from dash import Dash, html, dash_table
from dash.dependencies import Input,Output
from Dash_Handler import dash_handler
import Dash_components as dc
import dash_bootstrap_components as dbc
import pandas as pd


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([dc.Vol, dc.sidebar])


@app.callback(
    Output("Vol", "children"),
    [Input("input"+str(i), "value") for i in range(len(dc.Columns))],
)
def cb_render(*vals):
    result = dash_handler(vals)
    df1 = pd.DataFrame(result)
    return [
       dash_table.DataTable(
            df1.to_dict('records'),
            [{"name": i, "id": i} for i in df1.columns],
            fill_width=False
            
       ) 
    ]





if __name__=="__main__":
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)