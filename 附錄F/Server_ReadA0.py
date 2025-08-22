from machine import Pin,ADC
import network
import socket

SSID='Home'
PASSWORD='0492993493'
HOST = '0.0.0.0'
PORT = 80
def do_connect():
    global HOST
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
    HOST = sta.ifconfig()[0]
              
do_connect() # 連線基地台

httpResponse = b"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>NodeMCU-32S Server</title>
</head>
<body>
  光線強度: {value}<br>
</body>
</html>
"""

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

A0 = ADC(Pin(36)) # GPIO36 對應到 ADC0
A0.atten(ADC.ATTN_11DB)   #最大輸入電壓: 3.3v
A0.width(ADC.WIDTH_10BIT) #取樣範圍 0~1023

while True:
    client, addr = s.accept()
    value = A0.read() # 讀取 ADC0
    print("光線強度:{}" .format(value))
    client.send(httpResponse.format(value=value))    
    client.close()
    print()