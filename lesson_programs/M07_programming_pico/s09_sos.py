# SOS in Morse code with the onboard LED
from machine import Pin
import time

led = Pin("LED", Pin.OUT)
UNIT = 0.2                  # length of one dot in seconds


def flash(units):
    """LED on for a number of units, then a gap of 1 unit."""
    led.on()
    time.sleep(units * UNIT)
    led.off()
    time.sleep(UNIT)


S = [1, 1, 1]               # dot, dot, dot
O = [3, 3, 3]               # dash, dash, dash

while True:
    for letter in [S, O, S]:
        for units in letter:
            flash(units)
        time.sleep(2 * UNIT)    # gap between letters: 1 + 2 = 3 units
    time.sleep(4 * UNIT)        # gap between words: 3 + 4 = 7 units
