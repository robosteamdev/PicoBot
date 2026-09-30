# Scan both I2C buses of PicoBot and name the chips found
from machine import Pin, I2C

KNOWN = {0x40: "PCA9685 driver chip", 0x70: "PCA9685 call-to-all"}


def scan_bus(bus_id, sda, scl, board):
    i2c = I2C(bus_id, sda=Pin(sda), scl=Pin(scl), freq=400000)
    found = i2c.scan()
    print(f"I2C{bus_id} (SDA GP{sda}, SCL GP{scl}):")
    for address in found:
        name = KNOWN.get(address, "unknown chip")   # default text
        print(f"  {hex(address)} = {address}: {name}")
    if 0x40 in found:
        print("  OK -", board, "answers")
    else:
        print("  MISSING -", board, "- battery on? wires?")


scan_bus(0, 20, 21, "motor driver board")
scan_bus(1, 2, 3, "servo driver board")
