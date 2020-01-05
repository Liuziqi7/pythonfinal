import plotly as py
import cufflinks as cf
import pandas as pd
from flask import Flask
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline, Grid, Page
from flask import render_template, request

app = Flask(__name__)


@app.route('/gzsr')
def index_bar():
    df = pd.read_csv('./static/data/average_salary.csv', index_col=0, error_bad_lines=False)
    tl = Timeline()
    for i in range(2013, 2019):
        map0 = (
            Map()
                .add(
                "average_salary", list(zip(list(df.index), list(df["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年平均工资".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=20000, max_=100000),

            )
        )
        tl.add(map0, "{}".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text=''' 分析2013年到2018年人们生活水平的变化''',
                           text1='''首先从地图轮播的图表来看，北京和上海始终处于高收入的地区，而西藏从2015年开始有非常明显的提升。
                        到了2017年，我国各地的平均年收入基本达到了六万左右，并且逐年递增。''')


@app.route('/bar')
def index_bar_every_1_tp():
    df = pd.read_csv("./static/data/spending.csv")
    data1_x = df.columns.values[1:]

    x = list(df.指标)
    bar = (
        Bar()
            .add_xaxis(x)
            .set_global_opts(title_opts=opts.TitleOpts(),
                             datazoom_opts=opts.DataZoomOpts())
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    for key in data1_x:
        bar.add_yaxis(key, df[key].values.tolist())
    return render_template('index.html',
                           myechart=bar.render_embed(),
                           text='''
                           观察城镇居民人均消费支出的变化
                           ''', text1='''城镇居民人均可支配收入以及城镇居民人均消费支出在2013年到2018年之间有一定的增长，增长幅度没有明显的变化。''')


@app.route('/')
def index_bar_every():
    df = pd.read_csv('./static/data/average_salary.csv')
    tl = Timeline()
    for i in range(2013, 2019):
        map0 = (
            Map()
                .add(
                "average_salary", list(zip(list(df.area), list(df["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年平均工资".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=20000, max_=100000),

            )
        )
        tl.add(map0, "{}".format(i))

    return render_template('index.html',
                           myechart=tl.render_embed(),
                           result=df.values.tolist(),
                           a=1,
                           data_x=df.columns.values.tolist()[1:]
                           )

@app.route('/data')
def index_bar_every1():
    df = pd.read_csv('./static/data/average_salary.csv')
    tl = Timeline()
    for i in range(2013, 2019):
        map0 = (
            Map()
                .add(
                "average_salary", list(zip(list(df.area), list(df["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年平均工资".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=20000, max_=100000),

            )
        )
        tl.add(map0, "{}".format(i))

    return render_template('index_1.html'
                           )



if __name__ == '__main__':
    app.run(debug=True)
