# Read the temperature sensor inside the chip, once per second
from machine import ADC
import time

sensor = ADC(4)                 # channel 4 = temperature sensor

while True:
    raw = sensor.read_u16()     # 0 ... 65535
    voltage = raw * 3.3 / 65535
    temp = 27 - (voltage - 0.706) / 0.001721
    print(f"raw {raw}  {voltage:.4f} V  {temp:.1f} °C")
    time.sleep(1)
