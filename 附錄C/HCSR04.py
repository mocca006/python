from machine import Pin
import machine,time

echoTimeout = 23200 #等待截止時間
trigPin = Pin(0, mode=Pin.OUT) #觸發腳位 GPIO0
echoPin = Pin(4, mode=Pin.IN)  #回應腳位 GPIO4
trigPin.value(0)

def distance():
    trigPin.value(1) # 送出 10 us 的觸發訊號
    time.sleep_us(10)
    trigPin.value(0)
    # 計算高電位脈衝的時間
    pulseTime = machine.time_pulse_us(echoPin, 1, echoTimeout)
    if pulseTime > 0:
        return pulseTime / 58  # 公分換算
    else:
        return pulseTime  # 傳回 -1或-2

while True:
    cm = distance()
    if cm > 0:
        print('距離:%5.1f 公分' % cm)        
    else:
        print('讀取異常!')        
    time.sleep(1)  
    