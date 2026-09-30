# Measure the distance with the HC-SR04
# (based on the test program of the repository picobot-setup)
from machine import Pin, time_pulse_us
import time

trigger = Pin(27, Pin.OUT)      # Trig -> GP27
echo = Pin(26, Pin.IN)          # Echo -> GP26


def measure_distance():
    """Return the distance in cm, or None if no echo came back."""
    trigger.low()
    time.sleep_us(2)
    trigger.high()              # a 10 µs pulse starts a measurement
    time.sleep_us(10)
    trigger.low()
    # how long does Echo stay high? (give up after 30 000 µs)
    pulse = time_pulse_us(echo, 1, 30000)
    if pulse < 0:
        return None             # negative = timeout, no echo
    return pulse * 0.0343 / 2   # there and back: divide by 2


while True:
    d = measure_distance()
    if d is None:
        print("No echo")
    else:
        print("Distance: {:.1f} cm".format(d))
    time.sleep(0.5)
