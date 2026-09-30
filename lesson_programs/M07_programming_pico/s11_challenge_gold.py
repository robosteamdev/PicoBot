from machine import Pin, I2C
import time

led = Pin("LED", Pin.OUT)
BOARDS = [(0, 20, 21, "motor driver board"),
          (1, 2, 3, "servo driver board")]

missing = []
for bus_id, sda, scl, board in BOARDS:
    i2c = I2C(bus_id, sda=Pin(sda), scl=Pin(scl), freq=400000)
    if 0x40 not in i2c.scan():
        missing.append(board)

if len(missing) == 0:
    print("Self-test OK")
    led.on()
else:
    for board in missing:
        print("MISSING:", board)
    while True:                 # blink fast: something is wrong
        led.toggle()
        time.sleep(0.1)
