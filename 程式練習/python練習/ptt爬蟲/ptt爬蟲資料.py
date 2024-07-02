# -*- coding: utf-8 -*-
'''
1.抓取批踢踢實業坊›看板 Gossiping，最新的第1到第100筆的「標題、留言者以及連結網址」。
2.抓取批踢踢實業坊›看板 Gossiping，最舊的第1到第50筆，有「爆」標註的「標題、留言者以及連結網址」。
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
url=r'https://www.ptt.cc/bbs/Gossiping/index.html'
#最舊頁
url2=r"https://www.ptt.cc/bbs/Gossiping/index{}.html"
#表頭偽裝
a={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

#最新的第1到第100筆的「標題、留言者以及連結網址」
dd=[]
driver = webdriver.Chrome()
# 前往PTT頁面
driver.get(url)
#driver.add_cookie({"name": "over18", "value": "1"})
# 點擊確認滿18歲按鈕
button = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/button")
button.click()
# 爬取最新的第1到第100筆的「標題、留言者以及連結網址」
for g in range(1,10):
 print(f'等待3秒，爬取第 {g} 頁...')
 sleep(3)
 h1=driver.find_elements(By.CLASS_NAME,'r-ent')
 for post in h1:
     try:
        title_element = post.find_element(By.CLASS_NAME, 'title').find_element(By.TAG_NAME, 'a')
        title = title_element.text.strip() if title_element else 'N/A'

        author = post.find_element(By.CLASS_NAME, 'author').text.strip()

        link = 'https://www.ptt.cc' + title_element.get_attribute('href') if title_element else 'N/A'
        dd.append([title,author,link])
     except:
         title_element = post.find_element(By.CLASS_NAME, 'title')
         title = title_element.text.strip() if title_element else 'N/A'
         author = post.find_element(By.CLASS_NAME, 'author').text.strip()
         dd.append([title,author])
 if len(dd) >=100:
         break  
 # 點擊下一頁按鈕
 button = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/a[2]')
 button.click()
 # 關閉瀏覽器
driver.quit()

#最舊的第1到第50筆，有「爆」標註的「標題、留言者以及連結網址」
b=[]
i=0
while 1:
    i+=1
    print(f'等待3秒，爬取第 {i} 頁...')
    sleep(3)
    # 迴圈第一到五十筆
    url21=url2.format(i)
    print(url21)
    # 前往PTT頁面，用cookies
    r = requests.get(url21,cookies={'over18':'1'},headers=a)
    bs=BeautifulSoup(r.text,'lxml')
    # 有「爆」標註的文章
    data1=bs.find('div',class_='r-list-container action-bar-margin bbs-screen')
    data2 = data1.find_all('div',class_='r-ent')
    for k in data2:
        if k.find('div',class_='nrec').text=='爆':
           s1=k.find('a').text
           s2=k.find('div',class_='author').text
           s3='https://www.ptt.cc'+k.find('a')['href']
           b.append([s1,s2,s3])
    if len(b)>=50:
        break  
print('最新的第1到第100筆的「標題、留言者以及連結網址」:\n')
for y1 in dd[1:100]:
 print(y1) 
print('\n')   
print('最舊的第1到第50筆，有「爆」標註的「標題、留言者以及連結網址」:\n')
for y2 in b[1:50]:
 print(y2)

    
       
        
           
           
           
         
    