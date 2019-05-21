import pandas as pd

def path_analyse(filename,result):
    print("开始pandas路径分析")
    df = pd.read_csv(filename,\
        names = ['DriverID','OrderId','TimeStamp','Longitude','Latitude'])
    sc = df.sort_values(by = ['OrderId','TimeStamp'])
    sc[0:100000][['OrderId','Longitude','Latitude']]\
        .to_json(result,'split')

#path_analyse("D:\BigData\gps_20161101","gps.json")