# MicroPython: blink the LED on the Pico 2 W
from machine import Pin     # Pin controls the pins of the Pico
import time                 # time.sleep() waits

led = Pin("LED", Pin.OUT)   # "setup": runs once, from the top

while True:                 # "loop": repeat forever
    led.value(1)            # LED on
    time.sleep(0.5)         # wait 0.5 seconds
    led.value(0)            # LED off
    time.sleep(0.5)
