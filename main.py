import pandas as pd
import plotly.express as px
#data = [2,8,9,7,14,10]
#df = pd.DataFrame(data)
#print(df)
df = pd.read_csv("line_chart.csv")
fig = px.line(df, x="Year", y="Per capita income", color="Country", title="Per Capita Income")
fig.show()