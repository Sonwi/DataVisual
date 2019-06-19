import pandas as pd

# 把终点数据抽取到json数据文件中，用于热力图显示

def end_analyse(filename, result):
    print("开始pandas终点分析")
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp','SLongitude','SLatitude','ELongitude','ELatitude'])
    df[['ELongitude','ELatitude']].to_json(result,'split')
