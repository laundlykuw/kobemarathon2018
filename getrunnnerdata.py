import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import time

rank = pd.DataFrame()

for i in range(12, runner_id): #取得対象となるIDを参加者に配布されたカタログから確認して取得範囲を決めます
    try:
        url = "省略"

        dfs = pd.io.html.read_html(url)
        dfs[1].columns = ["key", "split", "rap"]

        template = pd.DataFrame(np.zeros(11).reshape(-1))
        template.columns = ["key"]

        temp = ["計測ポイント", "5km", "10km", "15km", "20km", "中間点", "25km", "30km", "35km", "40km", "Finish"]
        template.iloc[:,0] =temp

        df = pd.merge(dfs[1], template, on='key', how='right').fillna(0).T
        df_1 = dfs[0].iloc[:,1:].drop([1]).T
        df_1.index = [i]
        df_2 = pd.DataFrame(df.iloc[1,1:].append(df.iloc[2,1:])).T
        df_2.index = [i]
        df_ = pd.concat([df_1, df_2],axis=1)
        df_.index = [i]

        rank = pd.concat([rank, df_])
        print("id:{}".format(i))
    except:
        print("id:{}: data doesn't exist".format(i))
    time.sleep(1) #アクセスする間隔はすくなくとも1秒はあけるようにします。

rank.columns = ["sex","gross_time","net_time",
                "split_5km", "split_10km", "split_15km", "split_20km", "split_中間点",
                "split_25km", "split_30km", "split_35km", "split_40km", "split_Finish",
                "lap_5km", "lap_10km", "lap_15km", "lap_20km", "lap_中間点",
                "lap_25km", "lap_30km", "lap_35km", "lap_40km", "lap_Finish" ]
rank.to_csv("marathon_data.csv", header=True, index=True)
