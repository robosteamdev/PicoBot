# A tiny web server on PicoBot: it sends one page.
import network
import rp2
import socket
import time

rp2.country("BG")
SSID = "picobot-blue-sharks"
PASSWORD = "sharks2026"

ap = network.WLAN(network.AP_IF)
ap.config(essid=SSID, password=PASSWORD)
ap.active(True)
while not ap.active():
    time.sleep(0.1)
ip = ap.ifconfig()[0]
print("Open http://" + ip + "/ on your phone")

PAGE = """<!DOCTYPE html>
<html><head>
<meta name="viewport" content="width=device-width">
</head><body>
<h1>Hello from PicoBot!</h1>
</body></html>"""

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, 80))           # port 80 = the web port
server.listen(1)

while True:
    client, address = server.accept()     # wait for a browser
    request = client.recv(1024).decode()  # the request as text
    parts = request.split()               # split at the spaces
    if len(parts) > 1:
        path = parts[1]                   # e.g. "/" or "/forward"
    else:
        path = "/"
    print("Request for", path)
    client.send("HTTP/1.0 200 OK\r\n")
    client.send("Content-Type: text/html\r\n\r\n")
    client.send(PAGE)
    client.close()
