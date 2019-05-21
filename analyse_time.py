import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line

def analyse_time(filename):
    print("开始坐车长度时间分析")
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp',\
                'SLongitude','SLatitude','ELongitude','ELatitude'])
    data = [0 for i in range(20)]
    for i in range(0,len(df)-1):
        tem = round((int(df.iloc[i]['ETimeStamp']) - int(df.iloc[i]['STimeStamp']))/300)
        if tem<20:
            data[tem] += 1
    return data

def draw(data1,data2):
    attr = ['0-5min','5-10min','10-15min','15-20min','20-25min','25-30min','30-35min','35-40min','40-45min','45-50min','50-55min'\
        '55-60min','60-65min','65-70min','70-75min','75-80min','80-85min','85-90min','90-95min','95-100min']
    c = (Line().add_xaxis(attr).add_yaxis("2016_11_01",data1).add_yaxis("2016_11_05",data2).set_global_opts(title_opts=opts.TitleOpts(title="坐车时长分布折线图")))
    c.render("timeLine.html")
s1=analyse_time("D:\BigData\order_20161101")
s2=analyse_time("D:\BigData\order_20161105")
print(s2)
draw(s1,s2)