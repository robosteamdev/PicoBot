from machine import ADC
import time

sensor = ADC(4)
OFFSET = 0.0


def read_temperature():
    voltage = sensor.read_u16() * 3.3 / 65535
    return 27 - (voltage - 0.706) / 0.001721 + OFFSET


start = time.ticks_ms()
for i in range(10):
    temp = read_temperature()
    seconds = time.ticks_diff(time.ticks_ms(), start) // 1000
    with open("templog.csv", "a") as f:     # "a" = add at the end
        f.write(f"{seconds},{temp:.1f}\n")
    print(seconds, "s:", f"{temp:.1f}", "°C")
    time.sleep(2)
print("Saved in templog.csv")
