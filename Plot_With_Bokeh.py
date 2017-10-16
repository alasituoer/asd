#coding:utf-8
import pandas as pd
from adding_data import list_app_name

df = pd.read_csv('test.csv')

for app in list_app_name:
    df_t1 = df[['month', 'Index', app,]]
    df_t2 = df_t1[df_t1['Index']=='MIns']
    df_sorted = df_t2.sort_values(by='month')
    print df_sorted

