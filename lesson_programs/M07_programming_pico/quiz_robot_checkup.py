from machine import Pin, I2C
import network
import rp2
import time

led = Pin("LED", Pin.OUT)
led.off()

buses = [(0, 20, 21, "motor driver board"),
         (1, 2, 3, "servo driver board")]
for bus_id, sda, scl, board in buses:
    i2c = I2C(bus_id, sda=Pin(sda), scl=Pin(scl))
    found = i2c.scan()
    print("I2C" + str(bus_id) + ":")
    for address in found:
        print("  ", hex(address))
    if 0x40 in found:
        print("  OK -", board)
    else:
        print("  MISSING -", board)

rp2.country("BG")
ap = network.WLAN(network.AP_IF)
ap.config(essid="picobot-team7", password="team7pass")
ap.active(True)
while not ap.active():
    time.sleep(0.1)
led.on()
print("Network ready at", ap.ifconfig()[0])

while True:
    time.sleep(1)
