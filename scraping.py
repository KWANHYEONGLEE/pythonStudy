import requests
from bs4 import BeautifulSoup
import pymysql

url = 'https://eomisae.co.kr/fs'

response = requests.get(url)

if response.status_code == 200:
    #title, like정보 담을 배열만들기
    titleArray = []
    linkArray = []
    # title 정보 가져오기
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    titleDivs = soup.select('div.card_content')
    for titleDiv in titleDivs:
        title=titleDiv.select_one('h3>a')
        titleArray.append(title.get_text())

    # link 정보 가져오기
    linkDivs = soup.select('div.card_el')
    for linkDiv in linkDivs:
        link = linkDiv.select_one('a.pjax')
        linkArray.append(link['href'])
    
    
    # mysql에 연결해서 insert하기
    conn = pymysql.connect(host='localhost', user='root', password='kwan810326@', db='scraping', charset='utf8') 

    cursor = conn.cursor()

    for i in range(len(titleArray)):
        selectSql = "SELECT id FROM scraping WHERE title = %s"
        cursor.execute(selectSql,(titleArray[i]))
        if(cursor.fetchone()):
            print('있습니다.')
        else:
            print('없습니다.')
            sql = "INSERT INTO scraping (title,link) VALUES (%s,%s)"
            cursor.execute(sql,(titleArray[i],linkArray[i]))
            conn.commit()
    conn.close()
else : 
    print(response.status_code)