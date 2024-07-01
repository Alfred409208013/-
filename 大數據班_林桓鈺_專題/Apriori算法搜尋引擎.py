# -*- coding: utf-8 -*-
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
#操作搜尋物:CONVERSE CTAS MOVE 女鞋 低筒 高筒 厚底 帆布鞋 休閒鞋
# 指定 Excel 檔的路徑
excel_file_path = r"C:\Users\user\OneDrive\桌面\大數據隨身碟\29_林桓鈺_專題(最終)\生成資料處裡\生成資料.xlsx"
excel_c = r"C:\Users\user\OneDrive\桌面\大數據隨身碟\29_林桓鈺_專題(最終)\加權方式\顏色加權.xlsx"
excel_h = r"C:\Users\user\OneDrive\桌面\大數據隨身碟\29_林桓鈺_專題(最終)\加權方式\品牌加權.xlsx"

'''apriori演算法'''
# 定義市場籃資料（建立消費者資料）
dataset = [
    ['NIKE', 'CONVERSE', 'ADIDAS'],
    ['NIKE', 'NEW BALANCE'],
    ['CONVERSE', 'ADIDAS'],
    ['NIKE', 'NEW BALANCE', 'ADIDAS', 'FILA'],
    ['CONVERSE', 'ADIDAS', 'NEW BALANCE']
]

# 使用 TransactionEncoder 轉換數據集
def generate_df(dataset):
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    return df
#使用apriori製作頻繁項集
def apriori_frequent_itemsets(df):
 frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
 return frequent_itemsets
# 製作 apriori 的推薦方法
def apr(frequent_itemsets):
    frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: ', '.join(map(str, x)))
    frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].str.split(', ')
    df_expanded = frequent_itemsets['itemsets'].apply(pd.Series)
    df_expanded.columns = ['a1', 'a2']
    result_df = pd.concat([frequent_itemsets, df_expanded], axis=1)
    result_df.dropna(axis=0, inplace=True)
    del result_df['itemsets']
    return result_df
''''''

#使用pandas的read_excel函數讀取Excel檔
def load_data(excel_file_path, excel_c, excel_h):
    df1 = pd.read_excel(excel_file_path)
    dcolor = pd.read_excel(excel_c)
    dbrand = pd.read_excel(excel_h)
    return df1, dcolor, dbrand

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
def weighted(query, df1, dcolor, dbrand, apr_f_i):
    search_results = search(query, df1)
    if search_results.empty:
        return pd.DataFrame()

    merged_df = pd.merge(search_results, dcolor, how='left', on='color')
    merged_df = pd.merge(merged_df, dbrand, how='left', on='brand')

    merged_df['加權_x'] = merged_df['加權_x'].fillna(0)
    merged_df['加權_y'] = merged_df['加權_y'].fillna(0)
    '''將 Apriori 項集的結果應用到中'''
    for index, row in apr_f_i.iterrows():
        mask = merged_df['brand'].isin([row['a1'], row['a2']])
        merged_df.loc[mask, '加權_x'] += 10
    ''''''
    merged_df['加權'] = merged_df['加權_x'] + merged_df['加權_y']
    merged_df['weighted'] = merged_df['加權'].fillna(0)
    return merged_df.sort_values(by=['weighted'], ascending=False)

#處理多個關鍵字搜索並合併結果
def final(query, df1, dcolor, dbrand, apr_f_i):
    result_list = query.split()
    result_list_upper = [item.upper() for item in result_list]
    result_frames = [weighted(item, df1, dcolor, dbrand, apr_f_i) for item in result_list_upper]
    return pd.concat(result_frames, ignore_index=True)

#根據關鍵字調整色彩權重
def adjust_color_weights(query, dcolor):
    for item in query.split():
        if item.upper() in dcolor['color'].values:
            dcolor.loc[dcolor['color'] == item.upper(), '加權'] += 10
    return dcolor

#處理最後結果並返回必要信息
def end(query, df1, dcolor, dbrand, apr_f_i):
    dcolor = adjust_color_weights(query, dcolor)
    search_results = final(query, df1, dcolor, dbrand, apr_f_i)
    return search_results[['name', 'color', 'link']]
#主要函數
def main():
    df1, dcolor, dbrand = load_data(excel_file_path, excel_c, excel_h)
    df = generate_df(dataset)
    frequent_itemsets=apriori_frequent_itemsets(df)
    apr_f_i = apr(frequent_itemsets)
    query = input("輸入搜尋物:")
    result = end(query, df1, dcolor, dbrand, apr_f_i)
    return result

if __name__ == "__main__":
    consequent=main()
    print(consequent)
    

