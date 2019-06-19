import time
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

# 提取各时段的订单数量，画出折线图

def orderBarData(filename):
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

def draw(dis_list):
    print("开始绘制订单分布图")
    attr = ['0','1','2','3','4','5','6','7','8',\
        '9','10','11','12','13','14','15','16',\
        '17','18','19','20','21','22','23']
    bar = Line()
    bar.add_xaxis(attr).add_yaxis("1101订单数", dis_list).set_global_opts(title_opts=opts.TitleOpts(title="订单分布图"))
    print("结束绘制订单分布图")
    return bar

if __name__ == '__main__':
    dis_list = orderBarData("D:\BigData\order_20161101")
    bar = draw(dis_list)
    bar.render("orderLine.html")