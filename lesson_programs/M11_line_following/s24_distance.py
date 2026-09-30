# Distance with the HC-SR04: Trig = GP27, Echo = GP26
from machine import Pin, time_pulse_us
import time

trig = Pin(27, Pin.OUT, value=0)
echo = Pin(26, Pin.IN)


def distance_cm():
    """Distance in cm, or 999 when no echo comes back."""
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)                 # a 10 us pulse starts
    trig.value(0)                     # one measurement
    t = time_pulse_us(echo, 1, 30000) # echo time in us
    if t < 0:                         # no echo within 30 ms
        return 999
    return t * 0.0343 / 2


while True:
    print(round(distance_cm(), 1), "cm")
    time.sleep(0.5)
