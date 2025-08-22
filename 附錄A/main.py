from machine import Pin
import time 
 
# GPIO2對應到內建的LED 
led = Pin(2, Pin.OUT)
 
while True:
    led.value(1)   #燈亮
    time.sleep(0.5)#暫停 0.5 秒

    led.value(0)   #燈熄
    time.sleep(0.5)#暫停 0.5 秒
    print("Hello")