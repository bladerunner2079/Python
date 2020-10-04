
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# Generate plotting data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Setting data
data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=12,
        color='rgb(51,204,153)',
        symbol='pentagon',
        line=dict(
            width=2,
        )
    )
)]

# Setting layout
layout = go.Layout(
    title='Scatterplot', # Graph title
    xaxis=dict(title = 'Some random x-values'),
    yaxis=dict(title = 'Some random y-values'),
    hovermode='closest'
 )

# Plotting data
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="scatter_plot.html")

