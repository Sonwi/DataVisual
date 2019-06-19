import time
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# 选择三个不同的天气来统计订单数，可以对比分析天气对网约车的影响

def analyse(filename):
    print("开始pandas订单分布分析")
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp',\
                'SLongitude','SLatitude','ELongitude','ELatitude']) 
    dis_list = [0 for i in range(24)]
    for i in range(0,len(df)):
        dis_list[time.localtime(df.iloc[i]['STimeStamp']).tm_hour] += 1
    print("结束订单分析")
    return dis_list

def draw(d1,d2,d3,result):
    print("开始绘制订单分布图")
    attr = ['0','1','2','3','4','5','6','7','8',\
        '9','10','11','12','13','14','15','16',\
        '17','18','19','20','21','22','23']
    bar = Bar()
    bar.add_xaxis(attr).add_yaxis("1101订单数", d1).add_yaxis("1108订单数",d2).add_yaxis("1122订单数",d3).set_global_opts(title_opts=opts.TitleOpts(title="订单分布图"))
    bar.render(result)
    print("结束绘制订单分布图")

if __name__=='__main__':
    d1 = analyse("D:\BigData\order_20161101")
    d2 = analyse("D:\BigData\order_20161108")
    d3 = analyse("D:\BigData\order_20161122")
    draw(d1,d2,d3, "../templates/weatherBar.html")