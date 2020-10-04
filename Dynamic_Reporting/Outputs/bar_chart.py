import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Setting dataframe
df = pd.read_csv("../data/2018WinterOlympics.csv")

# Setting traces
trace0 = go.Bar(
    x=df["NOC"],
    y=df["Gold"],
    name="Gold",
    marker=dict(color="#FFD700")
)
trace1 = go.Bar(
    x=df["NOC"],
    y=df["Silver"],
    name="Silver",
    marker=dict(color="#9EA0A1")
)
trace2 = go.Bar(
    x=df["NOC"],
    y=df["Bronze"],
    name="Bronze",
    marker=dict(color="#CD7F32")
)

# Setting data
data = [trace0, trace1, trace2]

# Setting layout
layout = go.Layout(
    title="2018 Winter Olympics Medals by Country"
)

# Plotting data
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="bar_chart.html")

