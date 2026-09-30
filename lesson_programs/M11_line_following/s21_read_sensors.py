# Show the five values of the line sensor in the Shell
from machine import Pin
import time

# D1 ... D5 = GP8, GP9, GP13, GP14, GP15 (from RIGHT to LEFT)
PINS = [8, 9, 13, 14, 15]

sensors = []
for p in PINS:
    sensors.append(Pin(p, Pin.IN, Pin.PULL_UP))


def read_sensors():
    """Return a list of 5 values: 1 = this sensor sees the line."""
    values = []
    for s in sensors:
        values.append(s.value())
    return values


while True:
    print(read_sensors())
    time.sleep(0.2)
