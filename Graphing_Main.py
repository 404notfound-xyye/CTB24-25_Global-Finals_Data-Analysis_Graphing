import plotly.express as px
import pandas as pd

dt = pd.read_excel('/Users/alex.y/Documents/Github_Repo/CTB24-25_Global-Finals_Data-Analysis_Graphing/Base_Data/Excel+ALL+ENG.xlsx')

print(dt.head())
print(dt.info())
print(dt.describe())



# BarCharts - 表现前后均分差异
bar_c = px.bar(
    dt, 
    x="Participant Number", 
    y="Difference in Mean Performance Scores Pre- and Post-Intervention", 
    color="Group",
    title="Difference in Mean Performance Scores Pre- and Post-Intervention Between Groups",
    barmode='group',
    text="Difference in Mean Performance Scores Pre- and Post-Intervention"
)
bar_c.update_traces(
    texttemplate='%{text:.2f}', # 保留两位小数
    textposition='outside'
)
bar_c.update_xaxes(
    tickmode='linear'
)

bar_c.show()
bar_c.write_html("/Users/alex.y/Documents/Github_Repo/CTB24-25_Global-Finals_Data-Analysis_ChartsResult/BarCharts_表现前后均分差异/Bar+Difference_in_Mean_Performance_Scores_Pre-_and_Post-Intervention_Between_Groups.html")



# BoxPlots - 表现前后均分差异
box_p = px.box(
    dt, 
    x="Group", 
    y="Difference in Mean Performance Scores Pre- and Post-Intervention",
    title="Difference in Mean Performance Scores Pre- and Post-Intervention Between Groups",
    points="all"
)

box_p.show()
box_p.write_html("/Users/alex.y/Documents/Github_Repo/CTB24-25_Global-Finals_Data-Analysis_ChartsResult/BoxPlots_表现前后均分差异/Box+Difference_in_Mean_Performance_Scores_Pre-_and_Post-Intervention_Between_Groups.html")



# Histogram + 组间每日均分对比
his = px.histogram(
    dt,
    x="Days",
    y="Overall Daily Performance Mean Score",
    color="Group",
    title="Overall Daily Performance Scores Between Groups",
    barmode='group',
    text_auto=".2f", # 保留两位小数
    histfunc='avg' # histfunc默认sum，avg按照group计算每日均值
)

his.show()
his.write_html("/Users/alex.y/Documents/Github_Repo/CTB24-25_Global-Finals_Data-Analysis_ChartsResult/Histogram_组间每日均分对比/His+Overall_Daily_Performance_Scores_Between_Groups.html")



# LineCharts - 每日方面表现变化
metrics = [     # 折线绘制数据（列）
    "Learning Behaviors and Classroom Adaptation Mean Score",
    "Social Interaction Mean Score",
    "Emotion Regulation Mean Score",
    "Repetitive Behaviors and Interests Mean Score",
    "Overall Daily Performance Mean Score"
]
dt_mean = dt.groupby(["Days", "Group"], as_index=False)[metrics].mean() # 按Days/Group分组+计算分组中metrics列均值
dt_long = dt_mean.melt(     # 转换长格式，让每个metrics和days/group对应一行
    id_vars=["Days", "Group"],  # 保留列
    value_vars=metrics, # 数据分解到新列名对应原数据
    var_name="Metric", # 新列名
    value_name="Mean Score"  # 对应每个metric的分数
)
dt_accompanied = dt_long[dt_long["Group"] == "Accompanied Group"]   # 提取陪伴组数据
dt_non_accompanied = dt_long[dt_long["Group"] == "Non-Accompanied Group"] # 提取非陪伴组数据

# LineCharts - 陪伴组
line_acc = px.line(
    dt_accompanied, 
    x="Days", 
    y="Mean Score", 
    color="Metric",
    markers=True,  
    title="Performance Trends - Accompanied Group",
)
line_acc.update_xaxes(      # X-axis：保留整数Days
    tickmode="linear", 
    tick0=1, 
    dtick=1
)
line_acc.update_yaxes(      # Y-axis：两组范围一致
    range=[3.5, 8]
)

line_acc.show()
line_acc.write_html("/Users/alex.y/Documents/Github_Repo/CTB24-25_Global-Finals_Data-Analysis_ChartsResult/LineCharts_每日方面表现变化/Line+PerformanceTrends+WITH.html")

# LineCharts - 无陪伴组
line_non_acc = px.line(
    dt_non_accompanied, 
    x="Days", 
    y="Mean Score", 
    color="Metric",
    markers=True,  
    title="Performance Trends - Non-Accompanied Group",
)
line_non_acc.update_xaxes(      # X-axis：保留整数Days
    tickmode="linear", 
    tick0=1, 
    dtick=1
)
line_non_acc.update_yaxes(      # Y-axis：两组范围一致
    range=[3.5, 8]
)

line_non_acc.show()
line_non_acc.write_html("/Users/alex.y/Documents/Github_Repo/CTB24-25_Global-Finals_Data-Analysis_ChartsResult/LineCharts_每日方面表现变化/Line+PerformanceTrends+NON.html")