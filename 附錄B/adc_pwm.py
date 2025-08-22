from machine import Pin,ADC,PWM
import time

led = PWM(Pin(2), freq=1000) # GPIO2對應到內建的LED
A0 = ADC(Pin(36)) # GPIO36 對應到 ADC0
A0.atten(ADC.ATTN_11DB)   #最大輸入電壓: 3.3v
A0.width(ADC.WIDTH_10BIT) #取樣範圍 0~1023

while True:
  value = A0.read() #讀取A0埠
  print(value)      #顯示讀取的數值
  led.duty(value)   #亮度
  time.sleep(0.1) 