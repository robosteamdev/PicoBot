# Parking sensor: the LED blinks faster when an object is closer
from machine import Pin, time_pulse_us
import time

trigger = Pin(27, Pin.OUT)      # Trig -> GP27
echo = Pin(26, Pin.IN)          # Echo -> GP26
led = Pin("LED", Pin.OUT)       # the green LED on the Pico


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


while True:
    d = measure_distance()
    if d is None or d > 60:
        led.off()               # nothing close: LED off
        time.sleep_ms(100)
    elif d < 10:
        led.on()                # very close: LED stays on
        time.sleep_ms(100)
    else:
        pause = int(d * 10)     # 10 cm -> 100 ms, 60 cm -> 600 ms
        led.on()
        time.sleep_ms(50)
        led.off()
        time.sleep_ms(pause)
