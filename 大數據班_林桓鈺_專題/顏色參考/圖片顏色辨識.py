# -*- coding: utf-8 -*-
from colorthief import ColorThief
import requests
import pandas as pd
#rgb轉換函數 將rgb數值轉換為十六進制顏色
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
#獲取圖片中顏色並輸出RGB
def color(d):
    # 實際圖片的 URL
    new_image_url = f"{d}"

    # 使用 requests 下載圖片
    response = requests.get(new_image_url)

    # 將圖片保存到本地文件
    with open('temp_image.png', 'wb') as f:
        f.write(response.content)

    # 使用 ColorThief 獲取主要顏色
    color_thief = ColorThief('temp_image.png')
    dominant_color = color_thief.get_color(quality=1)

    #想獲取調色板中的顏色
    palette = color_thief.get_palette(color_count=6)
    # 將 dominant_color 和 palette 包裝在元組中進行返回
    return dominant_color, palette

# 測試函數
d = r'https://www.colorgg.com/img/000000.png'
result = color(d)
# 輸出 RGB 值
s1=list(result[0])
print("主要顏色 (RGB):",s1)
# 獲取調色板中的顏色
s2=result[1]
s21=[list(i) for i in s2]
print("調色板 (RGB):",s21)

#將RGB數值轉換為十六進制顏色
s1_hex= rgb_to_hex(s1)
print("主要顏色 (Hex):", s1_hex.upper())
s2_hex=[rgb_to_hex(j).upper() for j in s2]
print("主要顏色 (Hex):", s2_hex)


