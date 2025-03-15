import plotly.express as px
import pandas as pd

dt = pd.read_excel('/Users/alex.y/Documents/Github_Repo/G10_CTB_Global-Finals_Data-Analysis/Base_Data/Excel+ALL+ENG.xlsx')

print(dt.head())
print(dt.info())
print(dt.describe())

fig = px.bar(dt, x="Participant Number", y="Difference in Mean Performance Scores Pre- and Post-Intervention", color="Group",title="Difference in Mean Performance Scores Pre- and Post-Intervention Between Groups",barmode='group',text="Difference in Mean Performance Scores Pre- and Post-Intervention")
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_xaxes(tickmode='linear')
fig.show()

#fig = px.box(dt, x="Group", y="Difference in Mean Performance Scores Pre- and Post-Intervention",title="Difference in Mean Performance Scores Pre- and Post-Intervention Between Groups")
#fig.show()

#fig = px.histogram(dt,x="Days",y="Overall Daily Performance Mean Score\t",color="Group",title="Overall Daily Performance Scores Between Groups",barmode='group',text_auto=False)
#fig.show()

#fig = px.line(dt, x='天数', y='lifeExp', color='country', markers=True)
#fig.show()
