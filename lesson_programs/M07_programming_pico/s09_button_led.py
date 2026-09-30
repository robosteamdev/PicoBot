# The LED is on while the BOOTSEL button is pressed
import rp2
from machine import Pin
import time

led = Pin("LED", Pin.OUT)

while True:
    if rp2.bootsel_button() == 1:   # pressed?
        led.on()
    else:
        led.off()
    time.sleep_ms(10)               # check 100 times per second
