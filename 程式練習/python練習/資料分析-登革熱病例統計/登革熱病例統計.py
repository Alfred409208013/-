'''
請撰寫一程式，讀取登革熱近12個月每日確定病例統計read.csv，接著依序輸出下列項目：
a. 以遞減順序顯示居住縣市的病例人數
b. 顯示感染病例人數最多的5個國家，並按遞減順序顯示
c. 顯示台北市各區病例人數
d. 顯示台北市最近病例的日期

'''
import pandas as pd  

# 讀取CSV檔案，分隔符號為逗號
df1 = pd.read_csv('read.csv', encoding="utf-8", sep=",", header=0)

# 以"居住縣市"為分組依據，計算每個縣市的記錄數，並按數量降序排列
df_county = df1.groupby("居住縣市")["居住縣市"].count()
print(df_county.sort_values(ascending=False))

# 以"感染國家"為分組依據，計算每個國家的記錄數，並按數量降序排列，並列印前五個
df_country = df1.groupby("感染國家")["感染國家"].count()
print(df_country.sort_values(ascending=False).head(5))

# 選擇"居住縣市"為"台北市"的記錄
df_taipei = df1[df1.居住縣市 == "台北市"]

# 以"居住鄉鎮"為分組依據，計算"台北市"內每個鄉鎮的記錄數
print(df_taipei.groupby("居住鄉鎮")["居住鄉鎮"].count())

# 找出"台北市"內的最大發病日並列印
print("發病日: " + df_taipei.發病日.max()) 
