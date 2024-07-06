# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

products = []  # 創建一個空列表，用於存儲爬取的產品信息
url = 'https://ecshweb.pchome.com.tw/search/v3.3/'
def pc(search_query):
 url_search = f'{url}?q={search_query}&scope=all'

 # 使用 Chrome 瀏覽器驅動程式
 driver = webdriver.Chrome()

 try:
     # 前往搜尋結果頁面
     driver.get(url_search)

     # 等待一段時間，確保頁面元素都載入完成
     time.sleep(5)

     # 使用 JavaScript 滾動到頁面底部，模擬滾動載入更多商品
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

     # 再次等待一段時間
     time.sleep(10)

     # 取得商品列表
     products_elements = driver.find_elements(By.CLASS_NAME, 'col3f')
     '''
     欄位	代表意思
     name	    商品名稱
     describe	商品描述
     price	    商品價格
     color       商品顏色
     picB	    商品圖片(主圖)   
     Link        連結網址

     '''
     for product_element in products_elements:
         name_element = product_element.find_element(By.CLASS_NAME, 'prod_name').find_element(By.TAG_NAME, 'a')
         describe_element = product_element.find_element(By.CLASS_NAME, 'nick')
         price_element = product_element.find_element(By.CLASS_NAME, 'c3f').find_element(By.CLASS_NAME, 'price_box')
         link = name_element.get_attribute('href') if name_element else 'N/A'
         picB = product_element.find_element(By.CLASS_NAME, 'c1f').find_element(By.TAG_NAME, 'a').find_element(By.TAG_NAME, 'img').get_attribute('src') if product_element else 'N/A'
         # 取得文字內容，使用 .strip() 移除多餘的空白字符
         name = name_element.text.strip() if name_element else 'N/A'
         describe = describe_element.text.strip() if describe_element else 'N/A'
         price = price_element.text.strip() if price_element else 'N/A'
         products.append({
             'name': name,
             'describe': describe,
             'price': price,
             'link': link,
             'color':"n",
             'picB': picB
         })

 finally:
     # 關閉瀏覽器視窗
     driver.quit()

 # 印出爬取結果
 for product in products:
     print(product)
 return products



# 搜尋女鞋品項
a = pc('女鞋')
# 搜尋中性鞋品項
b = pc('中性鞋')
c=a+b

labels = ["name",'describe','price','link','color','picB']
try:
  with open("pchone.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in c:
            writer.writerow(elem)
except IOError:
    print("I/O error")

