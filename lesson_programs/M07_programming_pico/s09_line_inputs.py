# Show the five line-sensor channels, from left to right
from machine import Pin
import time

PINS = [15, 14, 13, 9, 8]       # D5 (left) ... D1 (right)

sensors = []
for number in PINS:
    sensors.append(Pin(number, Pin.IN, Pin.PULL_UP))

while True:
    values = []
    for s in sensors:
        values.append(s.value())    # 1 = line, 0 = no line
    print("left", values, "right")
    time.sleep(0.2)
