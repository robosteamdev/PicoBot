# Temperature logger: a timer measures every 2 s
from machine import ADC, Timer
import time

sensor = ADC(4)
OFFSET = 0.0            # your calibration offset from part C
readings = []           # the timer adds the values here


def read_temperature():
    voltage = sensor.read_u16() * 3.3 / 65535
    return 27 - (voltage - 0.706) / 0.001721 + OFFSET


def log(t):             # callback: measure and store, nothing more
    readings.append(read_temperature())


timer = Timer(period=2000, mode=Timer.PERIODIC, callback=log)
print("Logging 10 values, one every 2 s ...")
shown = 0
try:
    while shown < 10:
        if len(readings) > shown:           # a new value has arrived
            print(f"{shown + 1}: {readings[shown]:.1f} °C")
            shown = shown + 1
        time.sleep_ms(50)
finally:
    timer.deinit()

values = readings[:10]                      # the first 10 values
print(f"min {min(values):.1f}  max {max(values):.1f}")
print(f"average {sum(values) / len(values):.1f} °C")
