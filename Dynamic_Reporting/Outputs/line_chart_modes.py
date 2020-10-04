import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Generate random data
random_x = np.linspace(0, 1, 100)
random_y = np.random.randn(100)

# Setting traces
trace0 = go.Scatter(
    x=random_x,
    y=random_y+5,
    mode="markers",
    name="markers"
)
trace1 = go.Scatter(
    x=random_x,
    y=random_y,
    mode="lines+markers",
    name="lines+markers"
)
trace2 = go.Scatter(
    x=random_x,
    y=random_y-5,
    mode="lines",
    name="lines"
)

# Setting data
data = [trace0, trace1, trace2]

# Setting layout
layout = go.Layout(
    title='Line chart showing three different modes'
)

# Plotting data
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename="line_chart_modes.html")

