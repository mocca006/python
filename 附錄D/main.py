from machine_i2c_lcd import I2cLcd
from machine import I2C,Pin,ADC
from time import sleep

DEFAULT_I2C_ADDR = 0x27 # 位址
A0 = ADC(Pin(36)) # GPIO36 對應到 ADC0
A0.atten(ADC.ATTN_11DB)   #最大輸入電壓: 3.3v
A0.width(ADC.WIDTH_10BIT) #取樣範圍 0~1023

i2c = I2C(1,scl=Pin(22), sda=Pin(21), freq=100000) 
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.clear()

while True:
  A0_value = A0.read() #讀取A0埠
  print(A0_value)      #顯示轉換後的數值  

  lcd.move_to(0, 0)    #(0,0) 位置
  lcd.putstr("A0=" + str(A0_value)  + "   ") 
  sleep(0.5)