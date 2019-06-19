import pandas as pd

# 把起点数据抽取到json数据文件中，用于热力图显示

def start_analyse(filename,result):
    print("开始pandas起点分析")
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp','SLongitude','SLatitude','ELongitude','ELatitude'])
    df[['SLongitude','SLatitude']].to_json(result,'split')
    print("结束pandas起点分析")


