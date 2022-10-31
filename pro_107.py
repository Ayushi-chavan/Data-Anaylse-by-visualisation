import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("data1.csv")

print(df.groupby("level")['attempt'].mean())



fig = px.scatter(df.groupby("level")['attempt'].mean(), x='student_id', y='level',color='attempt',size_max=60)
fig.show()