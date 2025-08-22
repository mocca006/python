from machine import Pin, ADC
from time import sleep

A0 = ADC(Pin(36)) # GPIO36 對應到 ADC0
A0.atten(ADC.ATTN_11DB)   #最大輸入電壓: 3.3v
A0.width(ADC.WIDTH_10BIT) #取樣範圍 0~1023

while True:
  A0_value = A0.read()  #讀取A0埠
  print(A0_value)
  sleep(0.1)