# Line sensor monitor: shows what the five sensors see
from machine import Pin
import time

# D1 ... D5 = GP8, GP9, GP13, GP14, GP15 (from RIGHT to LEFT)
PINS = [8, 9, 13, 14, 15]

sensors = []
for p in PINS:
    sensors.append(Pin(p, Pin.IN, Pin.PULL_UP))

while True:
    values = []                      # D1 ... D5
    for s in sensors:
        values.append(s.value())     # 1 = line, 0 = surface

    picture = ""
    for n in range(4, -1, -1):       # D5 (left) first, D1 last
        if values[n] == 1:
            picture = picture + " #"
        else:
            picture = picture + " ."

    print("left" + picture + "  right    D1..D5 =", values)
    time.sleep(0.2)
