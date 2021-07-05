from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
url_a="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="

def alert():
   input= ent.get()
   intInput=int(input)

   for i in range(3,9):
      print(i)
      intP=intInput+i
      input_for=str(intP)
      req=requests.get(url_a+input_for)
      soup = BeautifulSoup(req.text ,"html.parser")
      test2=soup.find("div",attrs= {"class","win_result"}).get_text()
      test3= test2.split("\n")
      test4= test3[7:13]
      print(test4)

win.geometry("1000x1000")
win.title('kwan')
win.option_add("*Font","궁서 20")

#버튼 만들기
btn=Button(win)
btn.config(text="현재시각")
btn.config(width =20)
btn.config(command=alert)

#입력창 만들기
ent= Entry(win)


#화면에 넣기
ent.pack()
btn.pack()


win.mainloop()