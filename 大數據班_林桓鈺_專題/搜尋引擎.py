# -*- coding: utf-8 -*-
import pandas as pd
#操作搜尋物:CONVERSE CTAS MOVE 女鞋 低筒 高筒 厚底 帆布鞋 休閒鞋 
# 指定Excel檔的路徑
excel_file_path = r"C:\Users\user\OneDrive\桌面\大數據隨身碟\29_林桓鈺_專題(最終)\生成資料處裡\生成資料.xlsx"
excel_c = r"C:\Users\user\OneDrive\桌面\大數據隨身碟\29_林桓鈺_專題(最終)\加權方式\顏色加權.xlsx"
excel_h = r"C:\Users\user\OneDrive\桌面\大數據隨身碟\29_林桓鈺_專題(最終)\加權方式\品牌加權.xlsx"
#使用pandas的read_excel函數讀取Excel檔
def read_data():
    try:
        df1 = pd.read_excel(excel_file_path)
        dcolor = pd.read_excel(excel_c)
        dbrand = pd.read_excel(excel_h)
        return df1, dcolor, dbrand
    except Exception as e:
        print(f"Error reading Excel files: {e}")
        return None, None, None
#在文檔中搜尋關鍵字並返回結果
def keyword_search(query, documents):
    results = {}
    for doc_id, doc_text in documents.items():
        if query.lower() in doc_text.lower():
            results[doc_id] = doc_text
    return results
#在數據庫中搜索關鍵字
def search(query, df1):
    search_results = keyword_search(query, df1['name'])
    indices = list(search_results.keys())
    return df1.iloc[indices]
#將資料加權後進行排序
def weighted(query, df1, dcolor, dbrand):
    search_results = search(query, df1)
    if search_results.empty:
        return pd.DataFrame()

    merged_df = pd.merge(search_results, dcolor, how='left', on='color')
    merged_df = pd.merge(merged_df, dbrand, how='left', on='brand')
    merged_df['加權_x'] = merged_df['加權_x'].fillna(0)
    merged_df['加權_y'] = merged_df['加權_y'].fillna(0)
    merged_df['加權'] = merged_df['加權_x'] + merged_df['加權_y']
    merged_df['weighted'] = merged_df['加權'].fillna(0)
    del merged_df['加權'], merged_df['加權_x'], merged_df['加權_y']
    return merged_df.sort_values(by=['weighted'], ascending=False)
#處理多個關鍵字搜索並合併結果
def final(query, df1, dcolor, dbrand):
    result_list = query.split()
    result_frames = [weighted(item.upper(), df1, dcolor, dbrand) for item in result_list]
    return pd.concat(result_frames, ignore_index=True)
#根據關鍵字調整色彩權重
def adjust_color_weights(query, dcolor):
    for item in query.split():
        if item.upper() in dcolor['color'].values:
            dcolor.loc[dcolor['color'] == item.upper(), '加權'] += 10
    return dcolor
#處理最後結果並返回必要信息
def end(query, df1, dcolor, dbrand):
    updated_dcolor = adjust_color_weights(query, dcolor)
    search_results = final(query, df1, updated_dcolor, dbrand)
    return search_results[['name', 'color', 'link']]
#主要函數
def main():
    df1, dcolor, dbrand = read_data()
    if df1 is None or dcolor is None or dbrand is None:
     return

    query = input("輸入搜尋物:")
    result = end(query, df1, dcolor, dbrand)
    return result
if __name__ == "__main__":
    consequent=main()
    print(consequent)
    



