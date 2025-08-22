from machine_i2c_lcd import I2cLcd
from machine import I2C,Pin

# i2c = I2C(1, freq=100000)
i2c = I2C(1,scl=Pin(22), sda=Pin(21), freq=100000) 
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()

lcd.move_to(0, 0)  #(0,0) 位置
lcd.putstr("Hello World!") 