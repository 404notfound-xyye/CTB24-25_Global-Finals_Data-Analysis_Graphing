import plotly.express as px
import pandas as pd

dt = pd.read_excel('/Users/alex.y/Documents/Github_Repo/G10_CTB_Global-Finals_Data-Analysis/Base_Data/Excel+ALL+ENG.xlsx')

print(dt.head())
print(dt.info())
print(dt.describe())

fig = px.bar(dt, x="参与者编号", y="表现均分前后差异", color="分组",title="Wide-Form Input",barmode='group')
fig.show()