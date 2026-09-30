# Take 10 readings and print the average and the spread
from machine import Pin, time_pulse_us
import time

trigger = Pin(27, Pin.OUT)      # Trig -> GP27
echo = Pin(26, Pin.IN)          # Echo -> GP26


def measure_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    pulse = time_pulse_us(echo, 1, 30000)
    if pulse < 0:
        return None
    return pulse * 0.0343 / 2


readings = []
for i in range(10):
    d = measure_distance()
    if d is not None:           # keep only good readings
        readings.append(d)
        print("Reading", i + 1, ":", round(d, 1), "cm")
    time.sleep_ms(60)           # wait for old echoes to die away

if len(readings) > 0:
    average = sum(readings) / len(readings)
    spread = max(readings) - min(readings)
    print("Average:", round(average, 1), "cm")
    print("Spread: ", round(spread, 1), "cm")
else:
    print("No echo at all")
