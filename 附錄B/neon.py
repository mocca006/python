from machine import Pin,PWM
import time
import random

pwmR = PWM(Pin(2),freq=1000) #GPIO2 紅燈
pwmG = PWM(Pin(0),freq=1000) #GPIO0 綠燈
pwmB = PWM(Pin(4),freq=1000) #GPIO4 藍燈

while True:
    R= random.randint(0,1023) # 產生 0~1023 的亂數
    G= random.randint(0,1023) # 產生 0~1023 的亂數
    B= random.randint(0,1023) # 產生 0~1023 的亂數

    pwmR.duty(R)
    time.sleep(0.1)
    pwmG.duty(G)
    time.sleep(0.1)
    pwmB.duty(B)
    time.sleep(0.1)    
    print(R,G,B)


