# -*- coding: utf-8 -*-
import pandas as pd

# 指定Excel檔的路徑
excel_file_path =r"C:\Users\user\OneDrive\桌面\生成資料.xlsx"

# 使用pandas的read_excel函數讀取Excel檔
df1= pd.read_excel(excel_file_path)


#製作顏色的加權方式
df_color = df1.drop_duplicates(subset=["color"])
df_color=df_color["color"]
df_color['weighted']= []
#輸出
df_color.to_excel('顏色加權.xlsx', index=False)


#製作品牌的加權方式
df_brand = df1.drop_duplicates(subset=["brand"])
df_brand=df_brand["brand"]
#輸出
df_brand.to_excel('品牌加權.xlsx', index=False)

