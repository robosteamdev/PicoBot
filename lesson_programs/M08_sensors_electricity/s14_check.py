# Take 50 readings and show how often each sensor saw the line
from machine import Pin
import time

PINS = [8, 9, 13, 14, 15]            # D1 ... D5 (right -> left)
NAMES = ["D1", "D2", "D3", "D4", "D5"]
READINGS = 50

sensors = []
for p in PINS:
    sensors.append(Pin(p, Pin.IN, Pin.PULL_UP))

counts = [0, 0, 0, 0, 0]
for i in range(READINGS):
    for n in range(5):
        counts[n] = counts[n] + sensors[n].value()
    time.sleep(0.02)                 # 50 readings in about 1 s

for n in range(5):
    percent = counts[n] * 100 // READINGS
    print(NAMES[n], "saw the line in", percent, "% of the readings")
