import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#載入csv文件
df = pd.read_csv(r"C:\Users\user\OneDrive\桌面\專題code\女鞋價格\Datafiniti_Womens_Shoes.csv")

#印出文件
df.head()
#印出可能可以用的變數
for col in df.columns:
    print(col)
'''
id - 產品編號
brand - 品牌名稱
colors- 產品顏色
imageURLs - 產品網址連結
prices.amountMax - 產品最高價格
prices.amountMin - 產品最低價格
prices.color - 销售價格對應的商品顏色
prices.currency - 售價幣值
prices.isSale - 產品是否打折
prices.merchants - 產品销售的商家
'''
#統計品牌出現頻率 df2
df2 = df['brand'].value_counts()
#強制顯示所有結果
pd.options.display.max_rows = 200
df2

#替換品牌名稱
df['brand']=df['brand'].replace({'Adidas Outdoor':'adidas','dr. scholls':"Dr. Scholl's",'Adidas':'adidas',
                                 'Brinley Co. Collection':'Brinley Co.', 'SKECHERS':'skechers',
                                               })

#再次檢查更改後的品牌信息
print(df['brand'].value_counts())

#產品最高價格減去產品最低價格並算出百分率

df['priceDif'] = df['prices.amountMax'] - df['prices.amountMin']
df['priceDif%'] = (df['prices.amountMax'] - df['prices.amountMin'])/df['prices.amountMax']
df.head()

#篩選有折價的
df_promo = df[df['priceDif'] > 0]
df_promo
# 使用正则表达式过滤数据框，只保留包含 'price'、'brand' 和 'id' 的列
df_promo = df_promo.filter(regex='price|brand|id')

# 打印過濾後的數據框
print(df_promo)

#主要品牌的出現頻率
df3=pd.DataFrame(df2)
#品牌顏色
colors = ['black', 'white', 'purple', 'pink', 'red', 'silver|gray|ash',
          'gold|bronze', 'green|olive', 'navy|blue', 'brown|coffe',
          'beige|almond', 'orange', 'yellow']
freq = []

for color in colors:
    cnt = df['colors'].str.contains(color).sum()
    freq.append(cnt)
    
fig, ax = plt.subplots(figsize = (6, 8))

sns.barplot(y = colors, x = freq, color = '#389DFF')

plt.show()
#品牌出現頻率
df3.to_csv('brand.csv', index=True)