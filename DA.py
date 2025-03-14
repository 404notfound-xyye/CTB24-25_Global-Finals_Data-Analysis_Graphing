import plotly.express as px
import pandas as pd

dt = pd.read_excel('/Users/alex.y/Documents/Github_Repo/G10_CTB_Global-Finals_Data-Analysis/Base_Data/Excel+ALL+ENG.xlsx')

print(dt.head())
print(dt.info())
print(dt.describe())

fig = px.bar(dt, x="参与者编号", y="表现均分前后差异", color="分组",title="Wide-Form Input",barmode='group',text_auto=True)
fig.show()

fig = px.box(dt, x="分组", y="表现均分前后差异")
fig.show()

fig = px.bar(dt,x="天数",y="全天表现均分",color="分组",title="组间每日表现均分",barmode='',text_auto=True)
fig.show()

#fig = px.line(dt, x='天数', y='lifeExp', color='country', markers=True)
#fig.show()
