# Blink the green LED on the Pico
from machine import Pin     # Pin controls the pins of the Pico
import time                 # time has the sleep() function

led = Pin("LED", Pin.OUT)   # the onboard LED is an output

while True:                 # repeat forever
    led.on()                # LED on
    time.sleep(0.5)         # wait 0.5 seconds
    led.off()               # LED off
    time.sleep(0.5)         # wait 0.5 seconds
