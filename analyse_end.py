import pandas as pd

def end_analyse(filename):
    print("开始pandas终点分析")
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp','SLongitude','SLatitude','ELongitude','ELatitude'])
    df[['ELongitude','ELatitude']].to_json("end.json",'split')

end_analyse("D:\BigData\order_20161101")
