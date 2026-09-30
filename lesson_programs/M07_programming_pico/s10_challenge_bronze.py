from machine import ADC, Pin
import time

sensor = ADC(4)
led = Pin("LED", Pin.OUT)


def read_temperature():
    voltage = sensor.read_u16() * 3.3 / 65535
    return 27 - (voltage - 0.706) / 0.001721


start_temp = read_temperature()
print(f"Start: {start_temp:.1f} °C")

while True:
    temp = read_temperature()
    if temp > start_temp + 2:
        led.on()
    else:
        led.off()
    print(f"{temp:.1f} °C")
    time.sleep(1)
