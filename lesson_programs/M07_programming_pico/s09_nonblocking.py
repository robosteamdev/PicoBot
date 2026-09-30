# Blink the LED AND count button presses at the same time
import rp2
from machine import Pin
import time

led = Pin("LED", Pin.OUT)
BLINK_MS = 500                    # the LED changes every 500 ms
last_blink = time.ticks_ms()      # when did the LED change last?
previous = 0
count = 0

while True:
    now = time.ticks_ms()

    # job 1: blink - only when 500 ms have passed
    if time.ticks_diff(now, last_blink) >= BLINK_MS:
        led.toggle()
        last_blink = now

    # job 2: watch the button - in every loop
    pressed = rp2.bootsel_button()
    if pressed == 1 and previous == 0:
        count = count + 1
        print("Presses:", count)
    previous = pressed

    time.sleep_ms(10)             # a short pause is fine
