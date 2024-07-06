"""
請撰寫一程式，爬取新北市警察機關名單，API連結如下：https://www.codejudger.com/target/5204.json
程式須輸出：新北市每一所警察機關的相關訊息：名稱、地址、聯絡電話、網站、資料更新時間。
"""
import requests
import json

# 使用 requests 取得 JSON 格式的資料
h = requests.get("https://www.codejudger.com/target/5204.json")

# 使用 json.loads() 方法將 JSON 格式的資料轉換為 Python 資料結構
Univ= json.loads(h.text)

# 印出新北市大專院校名單的標題
print("新北市警察機關名單：\n")

# 篩選出類型為 '警察機關' 的資料並印出相關資訊
for i in Univ:
    if i['type'] == '警察機關':
        print("名稱：{}".format(i['name']))
        print("地址：{}".format(i['address']))
        print("聯絡電話：{}".format(i['tel']))
        print("網站：{}".format(i['website']))
        print("資料更新時間：{}".format(i['update_date']))
        print()