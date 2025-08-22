from machine import Pin,TouchPad
import time

led = Pin(2, Pin.OUT) # GPIO2對應到內建的LED
t = TouchPad(Pin(15)) # GPIO15為觸控開關腳位

while True:
    val=t.read()
    print("value=",val)
    time.sleep_ms(10)
    if val<200:
        led.value(1) # 點亮LED
    elif val>400:
        led.value(0) # 關閉LED