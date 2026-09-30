# Average of 10 readings, for the calibration
from machine import ADC
import time

sensor = ADC(4)


def read_temperature():
    voltage = sensor.read_u16() * 3.3 / 65535
    return 27 - (voltage - 0.706) / 0.001721


values = []
for i in range(10):
    values.append(read_temperature())
    time.sleep(1)

average = sum(values) / len(values)
print(f"min {min(values):.1f}  max {max(values):.1f}")
print(f"average {average:.1f} °C")
