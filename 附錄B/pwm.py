from machine import Pin, PWM
import time
 
led = PWM(Pin(2),freq=1000) # GPIO2對應到內建的LED 

while True:
    for n in range(1024):       #燈漸亮
        led.duty(n)
        time.sleep_ms(5)
    for n in range(1023,-1,-1): #燈漸熄
        led.duty(n)
        time.sleep_ms(5)
    print("change")