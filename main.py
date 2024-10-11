# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from waitress import serve

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

app.title = "CODELCO | DGM - Contratos"

# Expose the Flask server
server = app.server

# App layout
app.layout = html.Div(children=[html.Img(src='assets/LogoCodelco.svg', style={"width":"35%"}),html.Img(src='assets/xd.jpg', style={"width":"35%"})], style={'display':'flex','justify-content': 'center', 'align-items': 'center','height':'100vh', 'width':"100vw"}),
    #html.Hr(),
    #dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='my-final-radio-item-example'),
    #dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    #dcc.Graph(figure={}, id='my-final-graph-example')


# Add controls to build the interaction
@callback(
    Output(component_id='my-final-graph-example', component_property='figure'),
    Input(component_id='my-final-radio-item-example', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    # Use Waitress for production
    print("App running on: http://localhost:10000")
    serve(server, host='0.0.0.0', port=10000)

