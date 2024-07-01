# -*- coding: utf-8 -*-
import pandas as pd
import csv
# 指定Excel檔的路徑
excel_file_path =r"C:\Users\user\OneDrive\桌面\momo0115.xlsx"
excel_file_path02 =r"C:\Users\user\OneDrive\桌面\pc0115.xlsx"
# 使用pandas的read_excel函數讀取Excel檔
df = pd.read_excel(excel_file_path)
dg = pd.read_excel(excel_file_path02)
#將價格轉成數字
df['price']=[int(i.replace(',', '')) for i in df['price']]
dfg=pd.concat([df, dg], ignore_index=True)
# 用字典形式指定要更改的列名
new_column_names = {'color01': 'color',}
dfg.rename(columns=new_column_names, inplace=True)
dfg.to_excel('生成資料.xlsx', index=False)