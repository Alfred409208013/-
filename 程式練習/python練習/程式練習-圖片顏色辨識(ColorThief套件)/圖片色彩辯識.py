# -*- coding: utf-8 -*-
from colorthief import ColorThief

# RGB轉換函數：將RGB數值轉換為十六進制顏色
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# 獲取圖片中顏色並輸出RGB
def get_colors(image_path):
    try:
        # 使用 ColorThief 獲取主要顏色
        color_thief = ColorThief(image_path)
        dominant_color = color_thief.get_color(quality=1)

        # 獲取調色板中的顏色
        palette = color_thief.get_palette(color_count=6)

        return dominant_color, palette

    except Exception as e:
        print(f"圖片處理失敗: {e}") 
        return None, None

# 測試函數
image_path = r"C:\Users\user\OneDrive\桌面\程式練習-圖片顏色辨識(ColorThief套件)\black.png" #放入圖片的路徑
dominant_color, palette = get_colors(image_path)

if dominant_color and palette:
    # 輸出主要顏色 (RGB)
    dominant_color_rgb = list(dominant_color)
    print("主要顏色 (RGB):", dominant_color_rgb)

    # 輸出調色板中的顏色 (RGB)
    palette_rgb = [list(color) for color in palette]
    print("調色板 (RGB):", palette_rgb)

    # 將RGB數值轉換為十六進制顏色
    dominant_color_hex = rgb_to_hex(dominant_color)
    print("主要顏色 (Hex):", dominant_color_hex.upper())

    palette_hex = [rgb_to_hex(color).upper() for color in palette]
    print("調色板 (Hex):", palette_hex)
else:
    print("未能獲取顏色資訊。")
