# basic overlaid area chart
import plotly.offline as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 6, 7, 8, 9, 10, 12],
    y=[2749 ,2552 ,5424 ,2647 ,1552 ,342 ,331 ,309 ,650 ,299],
    fill='tozeroy',
    
)
# trace2 = go.Scatter(
#     x=[1, 2, 3, 4],
#     y=[3, 5, 1, 7],
#     fill='tonexty'
# )
data = [trace1]
py.offline.plot(data, filename='basic-area', link_text="Aetna 2015")

