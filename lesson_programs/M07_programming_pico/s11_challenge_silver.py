import network
import rp2
import time
from machine import Pin

SSID = "picobot-myteam"
PASSWORD = "12345678"
rp2.country("BG")

led = Pin("LED", Pin.OUT)
ap = network.WLAN(network.AP_IF)
ap.config(essid=SSID, password=PASSWORD)
ap.active(True)
while not ap.active():
    time.sleep(0.1)

for i in range(3):              # ready: 3 quick flashes
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)
led.on()

print("=" * 30)
print("Network: ", SSID)
print("Password:", PASSWORD)
print("Address:  http://" + ap.ifconfig()[0] + "/")
print("=" * 30)

while True:
    time.sleep(1)
