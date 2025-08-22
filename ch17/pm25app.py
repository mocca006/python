from tkinter import *
from tkinter.ttk import *
import pandas as pd
import requests

df = pd.read_csv("https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=CSV")

def showWeather(event):
    chosite = cbVar.get()
    if chosite != '請選擇：':
        reStr = requests.get('https://pm25-jeng.vercel.app/pm25/' + chosite).text
        jsondata = eval(reStr)  #轉換為字典
        showdata = '測站名稱：' + jsondata['測站'] + '\n\n'
        showdata += '日期時間：' + jsondata['時間'] + '\n\n'
        showdata += 'PM2.5值：' + jsondata['PM2.5']
        labelVar.set(showdata)
    else:
        labelVar.set('請選擇測站！')

win = Tk()
win.title('PM2.5即時資料')
win.geometry('350x200')

cbVar = StringVar()
cb = Combobox(win, textvariable=cbVar)  #下拉選單元件
sitelist = df['site'].tolist()
combolist = []
combolist.append("請選擇：")
for site in sitelist:
    combolist.append(site)
cb['value'] = combolist  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', showWeather)  #設定選取選項後執行的程式
cb.place(x=80, y=40)

labelVar = StringVar()  
labelShow = Label(win, foreground='red', justify='left', textvariable=labelVar)  #標籤元件
labelVar.set('尚未選擇縣市！')
labelShow.place(x=80, y=80)

win.mainloop()


