from machine import Pin
import time

led = Pin("LED", Pin.OUT)
while True:
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.3)
