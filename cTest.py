import requests
from bs4 import BeautifulSoup
import re

#url 정의하기
url= "https://www.coupang.com/np/search?component=&q=휴지&channel=user"
url_test="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=959"
url_a="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=333"

cleanr =re.compile('<.*?>')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
req=requests.get(url,headers=headers)
soup = BeautifulSoup(req.text ,"html.parser")
# test2=soup.find("div",attrs= {"class","win_result"}).get_text()
# test3=soup.findAll("div",attrs={"class","rating-star"})
# test3=soup.findAll("strong",attrs={"class","price-value"})
test3=soup.find_all("dl",attrs={"class","search-product-wrap"})
# test4= soup.findAll("div",attrs={"class","price-wrap"})
# strTest=str(test3)
# cleantext = re.sub('<.*?>', '', strTest,0).strip()
# print(len(test4))
# strTest=str(test3[1].img)
# ss=strTest.split('src="//')
# tt=str(ss[1]).split('" width')
# print("//"+tt[0])
# print(test3[1].img)
v=test3[0]
qq=str(test3[0])
children = v.findChildren("div" , recursive=False)
print(children)
for child in children:
    print (child)

# for i in range(0,30):
#     strTest=str(test3[i].img)
#     ss=re.split('src="//',strTest)
#     if( i <= 7):
#         tt=str(ss[1]).split('" width')
#         print("//"+tt[0])
#     else:
#         tt=str(ss[1]).split('" data-src')
#         print("//"+tt[0])
    
