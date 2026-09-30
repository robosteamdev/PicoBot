from machine import Pin
import time

led = Pin("LED", Pin.OUT)
centre = Pin(13, Pin.IN, Pin.PULL_UP)     # D3, 1 = line

while True:
    led.value(centre.value())
    time.sleep_ms(20)
