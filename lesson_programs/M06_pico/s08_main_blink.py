# Save this program on the Pico as main.py
from machine import Pin
import time

led = Pin("LED", Pin.OUT)

for i in range(3):          # hello sign: 3 quick flashes
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)

time.sleep(1)

while True:                 # then blink slowly forever
    led.toggle()
    time.sleep(1)
