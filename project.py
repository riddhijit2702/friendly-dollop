import csv
import plotly.figure_factory as ff
import pandas as pd


df = pd.read_csv('cc.csv')
fig = ff.create_distplot([df['Weight(Pounds)'].tolist()],['X'],show_hist=False)

fig.show()
