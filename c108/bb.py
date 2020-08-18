import plotly.figure_factory as ff
import pandas as pd
import csv

rag = pd.read_csv("data.csv")
hi = ff.create_distplot([rag["Avg Rating"].tolist()], ["Avg Rating"])
hi.show()