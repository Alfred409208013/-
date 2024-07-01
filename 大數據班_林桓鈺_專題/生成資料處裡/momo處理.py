# -*- coding: utf-8 -*-
import pandas as pd

# 指定Excel檔的路徑
excel_file_path =r"C:\Users\user\OneDrive\桌面\MOMO.xlsx"

# 使用pandas的read_excel函數讀取Excel檔
df = pd.read_excel(excel_file_path)

# 打印 DataFrame
print(df)
#打印列名稱
print(df.columns)

a=df.columns
del df['Unnamed: 0']
del df['desc']
del df['款式']
del df['尺寸']
del df['品牌定位']
del df['cate']
del df['產地']
df=df.drop(["品牌系列","保固期","配件","材質","功能","price","對象與族群"], axis=1)
new_column_names = {'title': 'name', 'amount': 'price', '品牌名稱': 'describe',"顏色":"color"}
df.rename(columns=new_column_names, inplace=True)
df['brand']=df['brand'].replace({'NIKE 耐吉':'NIKE','baibeauty 白鳥麗子':"baibeauty",'adidas 愛迪達':'adidas',
                                 'GREEN PHOENIX 波兒德':'GREEN PHOENIX', 'SCANDINAVIAN FOREST 北歐小刺蝟':'SCANDINAVIAN FOREST',
                                 'MUJI 無印良品':'MUJI' ,'FUFA Shoes 富發牌':'FUFA Shoes','SNAIL 蝸牛':'SNAIL','PAMAX 帕瑪斯':'PAMAX','LE COQ SPORTIF 公雞':'LE COQ SPORTIF',
                                 'asics 亞瑟士':'asics','GOODYEAR 固特異':'GOODYEAR','SANDARU 山打努':'SANDARU','A.S.O 阿瘦集團':'A.S.O','MATERIAL 瑪特麗歐':'MATERIAL','VICTOR 勝利體育':'VICTOR'})
del df['describe']
# 刪除包含缺失值的行
df= df.dropna()
df['color01'] = df['color'].str.slice(0,1) 
df['color01']=df['color01'].replace({'多':'藍','米':"灰",'卡':'棕'})
del df['color02']
del df['color']
df.to_excel('momo0115.xlsx', index=False)
