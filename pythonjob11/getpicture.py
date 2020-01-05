from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import matplotlib.animation as animation
from IPython.display import HTML
import plotly as py

UPLOAD_FOLDER = "./data/"

def get_picture1():
    df=pd.read_csv(UPLOAD_FOLDER + "most population.csv",encoding='gbk')
    country=list(df.Country)
    year=list(df['2018'])
    各国人口密度=list(zip(country,year))
    ditu = (
        Map()
        .add("各国人口密度",各国人口密度, "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2018年"),
            visualmap_opts=opts.VisualMapOpts(max_=600),
        )
    )
    fig = ditu.render()
    return fig


def get_picture2():
    df=pd.read_csv(UPLOAD_FOLDER + "most population.csv",encoding='gbk')
    country=list(df.Country)
    year=list(df['1968'])
    各国人口密度=list(zip(country,year))
    ditu = (
        Map()
        .add("各国人口密度",各国人口密度, "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="1968年"),
            visualmap_opts=opts.VisualMapOpts(max_=600),
        )
    )
    fig = ditu.render()
    return fig


def get_picture3():
    df = pd.read_csv(UPLOAD_FOLDER + 'city populations.csv',encoding='utf-8',usecols=['name', 'group', 'year', 'value'])
    current_year = 1968
    dff = (df[df['year'].eq(current_year)]
        .sort_values(by='value', ascending=True)
        .head(10))
    colors = dict(zip(
        ['India', 'Europe', 'Asia', 'Latin America',
        'Middle East', 'North America', 'Africa'],
        ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
        '#aafbff', '#f7bb5f', '#eafb50']
    ))
    group_lk = df.set_index('name')['group'].to_dict()
    fig, ax = plt.subplots(figsize=(15, 8))
    dff = dff[::-1]   # 从上到下翻转值
    # 将颜色值传递给`color=`
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    # 遍历这些值来绘制标签和值(Tokyo, Asia, 38194.2)
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value, i,     name,            ha='right')  # Tokyo: 名字
        ax.text(value, i-.25, group_lk[name],  ha='right')  # Asia: 组名
        ax.text(value, i,     value,           ha='left')   # 38194.2: 值
    # 在画布右方添加年份
    ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')
    plt.savefig('./static/example1.png')
    

def get_picture4():
    df = pd.read_csv(UPLOAD_FOLDER + 'city populations.csv',encoding='utf-8',usecols=['name', 'group', 'year', 'value'])
    current_year = 2018
    dff = (df[df['year'].eq(current_year)]
        .sort_values(by='value', ascending=True)
        .head(10))
    colors = dict(zip(
        ['India', 'Europe', 'Asia', 'Latin America',
        'Middle East', 'North America', 'Africa'],
        ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
        '#aafbff', '#f7bb5f', '#eafb50']
    ))
    group_lk = df.set_index('name')['group'].to_dict()
    fig, ax = plt.subplots(figsize=(9, 5))
    dff = dff[::-1]   # 从上到下翻转值
    # 将颜色值传递给`color=`
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    # 遍历这些值来绘制标签和值(Tokyo, Asia, 38194.2)
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value, i,     name,            ha='right')  # Tokyo: 名字
        ax.text(value, i-.25, group_lk[name],  ha='right')  # Asia: 组名
        ax.text(value, i,     value,           ha='left')   # 38194.2: 值
    # 在画布右方添加年份
    ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')
    plt.savefig('./static/example2.png')
    
    return 'example2.html'


def get_picture5():
    df = pd.read_csv(UPLOAD_FOLDER + 'city populations.csv',encoding='utf-8',usecols=['name', 'group', 'year', 'value'])
    fig, ax = plt.subplots(figsize=(9, 5)) 
    colors = dict(zip(
        ['India', 'Europe', 'Asia', 'Latin America',
        'Middle East', 'North America', 'Africa'],
        ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
        '#aafbff', '#f7bb5f', '#eafb50']
    ))
    group_lk = df.set_index('name')['group'].to_dict()
    
    def draw_barchart(year):
        dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
        ax.clear()
        ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
        dx = dff['value'].max() / 200
        for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
            ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
            ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
            ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
        # ... polished styles
        ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
        ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
        ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        ax.xaxis.set_ticks_position('top')
        ax.tick_params(axis='x', colors='#777777', labelsize=12)
        ax.set_yticks([])
        ax.margins(0, 0.01)
        ax.grid(which='major', axis='x', linestyle='-')
        ax.set_axisbelow(True)
        plt.box(False)
    animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1968, 2019))
    
    return HTML(animator.to_jshtml())