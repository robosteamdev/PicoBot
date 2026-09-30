# Reaction-time game with the LED and the BOOTSEL button
import rp2
from machine import Pin
import time
import random

led = Pin("LED", Pin.OUT)
led.off()
print("Press BOOTSEL as soon as the LED lights up!")

wait_ms = random.randint(2000, 5000)    # random wait: 2 to 5 s
start_wait = time.ticks_ms()
too_early = False
while time.ticks_diff(time.ticks_ms(), start_wait) < wait_ms:
    if rp2.bootsel_button() == 1:       # pressed during the wait?
        too_early = True

if too_early:
    print("Too early! Run the program again.")
else:
    led.on()
    start = time.ticks_ms()
    while rp2.bootsel_button() == 0:    # wait for the press
        pass
    reaction = time.ticks_diff(time.ticks_ms(), start)
    led.off()
    print("Your reaction time:", reaction, "ms")
