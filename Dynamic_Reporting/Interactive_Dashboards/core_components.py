import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(
        options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "Montreal", "value": "MTL"},
            {"label": "London", "value": "LDN"}
        ],
        value="MTL"
    ),

    html.Label("Multi-Select Dropdown"),
    dcc.Dropdown(
        options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "Montreal", "value": "MTL"},
            {"label": "London", "value": "LDN"}
        ],
        value=["MTL", "LDN"],
        multi=True
    ),

    html.Label("Slider"),
    html.P(
        dcc.Slider(
            min=-5,
            max=10,
            step=0.5,
            marks={i: i for i in range(-5, 11)},
            value=-3
        )),

    html.Label("Radio Items"),
    dcc.RadioItems(
        options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "Montreal", "value": "MTL"},
            {"label": "London", "value": "LDN"}
        ],
        value="MTL"
    )
], style={"width": "50%"})

if __name__ == "__main__":
    app.run_server()


