import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Setting dataframe
df = pd.read_csv("../data/mpg.csv")
df["text1"] = pd.Series(df["model_year"], dtype=str)
df["text2"] = "'"+df["text1"]+" "+df["name"]

# Setting data
data = [go.Scatter(
    x=df["horsepower"],
    y=df["mpg"],
    mode="markers",
    marker=dict(size=1.5*df["cylinders"])
)]

# Setting layout
layout = go.Layout(
    title="Vechicle mpg vs horspower",
    xaxis=dict(title="Horsepower"),
    yaxis=dict(title="MPG"),
    hovermode="closest"
)

# Plotting data
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename="bubble_chart.html")

