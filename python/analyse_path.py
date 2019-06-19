import pandas as pd

# 把轨迹数据抽取到json数据文件中，用于轨迹图的可视化

def path_analyse(filename,result):
    print("开始pandas路径分析")
    df = pd.read_csv(filename,\
        names = ['DriverID','OrderId','TimeStamp','Longitude','Latitude'])
    sc = df.sort_values(by = ['OrderId','TimeStamp'])
    sc[0:100000][['OrderId','Longitude','Latitude']]\
        .to_json(result,'split')
