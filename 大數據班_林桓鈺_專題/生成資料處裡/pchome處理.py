# -*- coding: utf-8 -*-
import pandas as pd
excel_file_path02 =r"C:\Users\user\OneDrive\桌面\pchone0115.xlsx"
dg = pd.read_excel(excel_file_path02)
# 擷取多列
dg = dg[['name', 'price','link','picB']]
# 刪除包含缺失值的行
dg= dg.dropna()
dg['sm'] = dg['name'].str.extract(r'([a-zA-Z]+)')
dg= dg.dropna()
#更改名稱
dg['sm']=dg['sm'].replace({'New':'New Balance','K':'K-SWISS','G':'G.P'})
dg['brand']=dg['sm']
del dg['sm']
dg.to_excel('pc0115.xlsx', index=False)
