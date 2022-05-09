import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)

df = pd.read_csv("/home/zablon/Desktop/project/Dash/dash_intro/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

# App Layout
app.layout = html.Div([
    html.H1("Hello Dash"),

    dcc.Dropdown(id="slct_year",
                options=[
                    {"label": "2015", "value":2015},
                    {"label": "2016", "value":2016},
                    {"label": "2017", "value":2017},
                    {"label": "2018", "value":2018}],
                    multi=True,
                    value=2015,
                    style={'width':"40%"}
                    ),
    html.Div(id="output_container", children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})
])

# connecting components to plotly graphs
@app.callback(
    [Output(component_id='output_container', component_property='children'),
    Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]


    return container




if __name__ == '__main__':
    app.run_server(debug=True)