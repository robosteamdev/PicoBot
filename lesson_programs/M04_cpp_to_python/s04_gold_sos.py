# SOS with the LED of the Pico 2 W
from machine import Pin
import time

led = Pin("LED", Pin.OUT)
pattern = [200, 200, 200, 600, 600, 600, 200, 200, 200]  # ms

while True:                    # Arduino's loop()
    for t in pattern:
        led.value(1)
        time.sleep_ms(t)       # delay(pattern[i])
        led.value(0)
        time.sleep_ms(200)
    time.sleep_ms(2000)        # pause before the next SOS
