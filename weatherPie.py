import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

def analyse(filename):
    print("开始pandas订单分布分析")
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp',\
                'SLongitude','SLatitude','ELongitude','ELatitude']) 
    return len(df)


l = [0 for i in range(2)]
a = ["1101","1105"]
l[0] = analyse("D:\BigData\order_20161101")
l[1] = analyse("D:\BigData\order_20161105")
#l[2] = analyse("D:\BigData\order_20161122")
c =(Pie().add("",  [list(z) for z in zip(a,l)])
        .set_global_opts(title_opts=opts.TitleOpts(title="订单数量对比饼状图"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
c.render("Pie1.html")