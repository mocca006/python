from machine import Pin
from time import sleep
 
# GPIO2對應到內建的LED
led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN) #GPIO4

while True:
    if button.value()==0: #按下按鈕，燈亮
        led.value(1)
    else:  #放開按鈕，燈熄
        led.value(0)
    print(button.value())
    sleep(.1)    