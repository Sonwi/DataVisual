import pandas as pd

def start_analyse(filename):
    print("开始pandas起点分析")
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp','SLongitude','SLatitude','ELongitude','ELatitude'])
    df[['SLongitude','SLatitude']].to_json("start.json",'split')
    print("结束pandas起点分析")

start_analyse("D:\BigData\order_20161101")
