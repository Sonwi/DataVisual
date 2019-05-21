import pandas as pd
import time

def analyse(filename,result):
    df = pd.read_csv(filename,\
        names = \
            ['OrderId','STimeStamp','ETimeStamp',\
                'SLongitude','SLatitude','ELongitude','ELatitude']) 
    #sc = df[((time.localtime(df['STimeStamp']).tm_hour) == a)]
    sc = df[(df['STimeStamp'] >= 1477990800) & (df['STimeStamp'] < 1477994400)]
    sc[['SLongitude','SLatitude']].to_json(result,'split')

if __name__ == '__main__':
    analyse("D:\BigData\order_20161101","start17.json")