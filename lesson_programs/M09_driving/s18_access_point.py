# Start a Wi-Fi access point on PicoBot.
import network
import rp2
import time

rp2.country("BG")                 # your country code: BG, RO, SK, UA
SSID = "picobot-blue-sharks"      # your team's own network name!
PASSWORD = "sharks2026"           # at least 8 characters

ap = network.WLAN(network.AP_IF)  # AP = access point
ap.config(essid=SSID, password=PASSWORD)
ap.active(True)

while not ap.active():            # wait until the network is ready
    time.sleep(0.1)

print("Network", SSID, "is ready")
print("IP address:", ap.ifconfig()[0])
