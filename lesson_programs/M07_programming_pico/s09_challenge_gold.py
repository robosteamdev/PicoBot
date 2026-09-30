import rp2
from machine import Pin
import time
import random

led = Pin("LED", Pin.OUT)
times = []

for round_number in range(1, 6):
    print("Round", round_number, "- wait for the LED ...")
    led.off()
    time.sleep(1)
    wait_ms = random.randint(2000, 5000)
    start_wait = time.ticks_ms()
    too_early = False
    while time.ticks_diff(time.ticks_ms(), start_wait) < wait_ms:
        if rp2.bootsel_button() == 1:
            too_early = True
    if too_early:
        print("Too early - this round does not count")
        continue                        # go on with the next round
    led.on()
    start = time.ticks_ms()
    while rp2.bootsel_button() == 0:
        pass
    reaction = time.ticks_diff(time.ticks_ms(), start)
    print("Reaction:", reaction, "ms")
    times.append(reaction)
    while rp2.bootsel_button() == 1:    # wait until released
        pass

led.off()
if len(times) > 0:
    print("Best:", min(times), "ms")
    print("Average:", sum(times) // len(times), "ms")
else:
    print("No valid rounds")
