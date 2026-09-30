# Start a Wi-Fi access point with your own network name
import network
import rp2
import time
from machine import Pin

SSID = "picobot-myteam"      # CHANGE: your team's network name
PASSWORD = "12345678"        # at least 8 characters

rp2.country("BG")            # your country code: BG, RO, SK, UA ...

led = Pin("LED", Pin.OUT)
led.off()

ap = network.WLAN(network.AP_IF)    # the Wi-Fi chip as access point
ap.config(essid=SSID, password=PASSWORD)
ap.active(True)                     # switch the network on

while not ap.active():              # wait until it is ready
    time.sleep(0.1)

led.on()                            # LED on = network ready
print("Network:", SSID)
print("Password:", PASSWORD)
print("Robot address:", ap.ifconfig()[0])

while True:                         # keep the program running
    time.sleep(1)
