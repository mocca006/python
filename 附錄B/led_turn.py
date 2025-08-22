from machine import Pin
import time 

def show_led(led):
    led.value(1)    #燈亮
    time.sleep(0.5) #停0.5秒
    led.value(0)    #燈熄
 
ledR = Pin(2, Pin.OUT)  #GPIO2 紅燈
ledG = Pin(0, Pin.OUT)  #GPIO0 綠燈
ledB = Pin(4, Pin.OUT)  #GPIO4 藍燈
 
while True:
    show_led(ledR) # 紅燈亮
    show_led(ledG) # 綠燈亮
    show_led(ledB) # 藍燈亮
    print("R,G,B")