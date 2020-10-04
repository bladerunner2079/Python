
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

app = dash.Dash()

df = pd.read_csv("data/OldFaithful.csv")

app.layout = html.Div([
    dcc.Graph(
        id="old_faithful",
        figure={
            "data": [
                go.Scatter(
                    x=df["X"],
                    y=df["Y"],
                    mode="markers"
                )
            ],
            "layout": go.Layout(
                title = "Old Faithful Eruption Intervals versus Durations",
                xaxis={"title": "Duration of Eruption (minutes)"},
                yaxis={"title": "Interval to Next Eruption (minutes)"},
                hovermode="closest"
            )
        }
    )
])

if __name__ == "__main__":
    app.run_server()