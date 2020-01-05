from flask import Flask, render_template, request
from pyecharts.charts import Map, Geo, EffectScatter
from pyecharts import options as opts
import pandas as pd
import cufflinks as cf
import plotly as py
import getpicture
import json

app = Flask(__name__)

# 准备工作
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()
UPLOAD_FOLDER = "./data/"

@app.route('/getSelect', methods=['GET', 'POST'])
def get_select() -> 'html':
    select = {
        "picture1" : "人口密度地图",
        "picture5" :  "动态可视化图"
    }
    return json.dumps(select)
        

@app.route('/', methods=['GET'])
def get_index():
    df=pd.read_csv(UPLOAD_FOLDER + "most population.csv",encoding='gbk')
    data_str = df.to_html()
    with open('tittle.html', encoding="utf8", mode="r") as f:
        tittle = "".join(f.readlines())
    return render_template('results.html',
                            the_res = data_str,
                            the_tittle=tittle,
                           )


@app.route('/', methods=['POST'])
def show() -> 'html':
    tit=""
    the_select = request.form['the_region_selected']
    print(the_select)
    if(the_select=="picture1"):
        path1 = getpicture.get_picture1()
        with open(path1, encoding="utf8", mode="r") as f:
            plot_all1 = "".join(f.readlines())
        path2 = getpicture.get_picture2()
        analyse = './analyse/analyse1.html'
        with open(path2, encoding="utf8", mode="r") as f:
            plot_all2 = "".join(f.readlines())
    if(the_select=="picture3"):
        path = getpicture.get_picture3()
        path = getpicture.get_picture4()
        with open(path, encoding="utf8", mode="r") as f:
            plot_all1 = "".join(f.readlines())
        plot_all2=""
        analyse = './analyse/analyse3.html'
    if(the_select=="picture5"):
        plot_all1 = getpicture.get_picture5()
        path = getpicture.get_picture3()
        path = getpicture.get_picture4()
        with open(path, encoding="utf8", mode="r") as f:
            plot_all2 = "".join(f.readlines())
        tit = '<div style="text-align: center;margin-bottom: 30px;"><h1><span>The most populous cities in the world from 1500 to 2018</span></h1></div>'
        analyse = './analyse/analyse4.html'
 
    with open('tittle.html', encoding="utf8", mode="r") as f:
        tittle = "".join(f.readlines())

    with open(analyse, encoding="utf8", mode="r") as f:
        describe = "".join(f.readlines())

    # plotly.offline.plot(data, filename='file.html')
    return render_template('results.html', the_plot_all1=plot_all1,the_plot_all2=plot_all2,the_tittle=tittle,the_tit=tit,
                           the_describe=describe)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
