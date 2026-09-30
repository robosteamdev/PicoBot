from machine import Pin
import time

led = Pin("LED", Pin.OUT)
print("Lighthouse on")

while True:
    for i in range(3):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    time.sleep(2)
