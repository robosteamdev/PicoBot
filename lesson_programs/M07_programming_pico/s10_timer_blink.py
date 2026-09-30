# A timer blinks the LED while the main program counts
from machine import Pin, Timer
import time

led = Pin("LED", Pin.OUT)


def blink(t):               # the callback; t is the timer
    led.toggle()


timer = Timer(period=500, mode=Timer.PERIODIC, callback=blink)

try:
    for i in range(10):
        print("The main program counts:", i)
        time.sleep(1)
finally:
    timer.deinit()          # always stop the timer
    led.off()
