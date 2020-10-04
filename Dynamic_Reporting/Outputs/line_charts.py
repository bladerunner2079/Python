import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Setting dataframe
df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')

# Cleaning up dataframe
df = df[df["DIVISION"] == "1"]
df.set_index("NAME", inplace=True)
df = df[[col for col in df.columns if col.startswith("POP")]]

# Setting data
traces = [go.Scatter(
    x=df.columns,
    y=df.loc[name],
    mode="markers+lines",
    name=name
) for name in df.index]

# Setting layout
layout = go.Layout(
    title="Population Estimates of the Six New England States"
)

# Plotting data
fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig, filename="line_plot.html")

