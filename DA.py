import plotly.express as px
import pandas as pd


dt = pd.read_excel('/Users/alex.y/Documents/Github_Repo/G10_CTB_Global-Finals_Data-Analysis/Base_Data/Excel+ALL+ENG.xlsx')

print(dt.head())
print(dt.info())
print(dt.describe())

# Bar + 表现前后均分差异
fig = px.bar(
    dt, 
    x="Participant Number", 
    y="Difference in Mean Performance Scores Pre- and Post-Intervention", 
    color="Group",title="Difference in Mean Performance Scores Pre- and Post-Intervention Between Groups",
    barmode='group',
    text="Difference in Mean Performance Scores Pre- and Post-Intervention"
)
fig.update_traces(
    texttemplate='%{text:.2f}', 
    textposition='outside'
)
fig.update_xaxes(
    tickmode='linear'
)
fig.show()

# Boxplot + 表现前后均分差异
fig = px.box(
    dt, 
    x="Group", 
    y="Difference in Mean Performance Scores Pre- and Post-Intervention",
    title="Difference in Mean Performance Scores Pre- and Post-Intervention Between Groups",
    points="all"
)
fig.show()

# Histogram + 组间每日均分对比
fig = px.histogram(
    dt,
    x="Days",
    y="Overall Daily Performance Mean Score",
    color="Group",
    title="Overall Daily Performance Scores Between Groups",
    barmode='group',
    text_auto=".2f",
    histfunc='avg'
)
fig.show()

# Line
metrics = [
    "Learning Behaviors and Classroom Adaptation Mean Score",
    "Social Interaction Mean Score",
    "Emotion Regulation Mean Score",
    "Repetitive Behaviors and Interests Mean Score",
    "Overall Daily Performance Mean Score"
]

dt_mean = dt.groupby(["Days", "Group"], as_index=False)[metrics].mean()
dt_long = dt_mean.melt(id_vars=["Days", "Group"], value_vars=metrics, 
                        var_name="Metric", value_name="Mean Score")

dt_accompanied = dt_long[dt_long["Group"] == "Accompanied Group"]
dt_non_accompanied = dt_long[dt_long["Group"] == "Non-Accompanied Group"]

fig = px.line(
    dt_accompanied, 
    x="Days", 
    y="Mean Score", 
    color="Metric",
    markers=True,  
    title="Performance Trends - Accompanied Group",
    labels={"Days": "Dats", "Mean Score": "Mean Score"},
)
fig.show()

fig = px.line(
    dt_non_accompanied, 
    x="Days", 
    y="Mean Score", 
    color="Metric",
    markers=True,  
    title="Performance Trends - Non-Accompanied Group",
    labels={"Days": "Days", "Mean Score": "Mean Score"},
)
fig.show()