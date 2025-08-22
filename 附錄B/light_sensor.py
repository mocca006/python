from machine import Pin,ADC
import time

led = Pin(2, Pin.OUT) # GPIO2對應到內建的LED
A0 = ADC(Pin(36)) # GPIO36 對應到 ADC0
A0.atten(ADC.ATTN_11DB)   #最大輸入電壓: 3.3v
A0.width(ADC.WIDTH_10BIT) #取樣範圍 0~1023

while True:
  value = A0.read() #讀取A0埠
  print(value)      #顯示轉換後的數值
  if value<600:
      led.value(1)  #開燈
  else:
      led.value(0)  #關燈
  time.sleep(0.1) 