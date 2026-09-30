from machine import Pin
import time

led = Pin("LED", Pin.OUT)
team_number = 25


def blink(times):
    for i in range(times):
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)


while True:
    for digit in str(team_number):     # "25" -> "2", then "5"
        blink(int(digit))
        time.sleep(1.5)                # pause between the digits
    time.sleep(3)                      # long pause before the repeat
