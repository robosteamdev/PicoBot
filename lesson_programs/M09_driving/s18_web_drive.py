# Drive PicoBot from a web page on the phone.
import network
import rp2
import socket
import time
from picobot import PicoBot

rp2.country("BG")
SSID = "picobot-blue-sharks"      # your own name!
PASSWORD = "sharks2026"           # your own password!
SPEED = 40                        # slow and safe

robot = PicoBot()

PAGE = """<!DOCTYPE html>
<html><head>
<meta name="viewport" content="width=device-width">
<title>PicoBot</title>
<style>
body {font-family: Arial; text-align: center;}
a {display: inline-block; width: 28%; margin: 1%;
   padding: 24px 0; font-size: 20px; color: white;
   background: #1565C0; border-radius: 12px;
   text-decoration: none;}
a.stop {background: #C62828;}
</style></head><body>
<h2>PicoBot</h2>
<div><a href="/rotate_left">Turn L</a>
<a href="/forward">Forward</a>
<a href="/rotate_right">Turn R</a></div>
<div><a href="/left">Left</a>
<a class="stop" href="/stop">STOP</a>
<a href="/right">Right</a></div>
<div><a href="/back">Back</a></div>
</body></html>"""


def do_move(path):
    """Start the move that belongs to the path."""
    if path == "/favicon.ico":
        return                # the icon request: do nothing
    robot.stopRobot()         # always stop the old move first
    if path == "/forward":
        robot.goForward(SPEED)
    elif path == "/back":
        robot.goBackward(SPEED)
    elif path == "/left":
        robot.moveLeft(SPEED)
    elif path == "/right":
        robot.moveRight(SPEED)
    elif path == "/rotate_left":
        robot.rotateLeft(SPEED)
    elif path == "/rotate_right":
        robot.rotateRight(SPEED)
    # "/stop", "/" and all other paths: the robot stays stopped


ap = network.WLAN(network.AP_IF)
ap.config(essid=SSID, password=PASSWORD)
ap.active(True)
while not ap.active():
    time.sleep(0.1)
ip = ap.ifconfig()[0]
print("Connect to", SSID, "and open http://" + ip + "/")

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, 80))
server.listen(1)

try:
    while True:
        client, address = server.accept()
        request = client.recv(1024).decode()
        parts = request.split()
        if len(parts) > 1:
            path = parts[1]
        else:
            path = "/"
        print("Request for", path)
        do_move(path)
        client.send("HTTP/1.0 200 OK\r\n")
        client.send("Content-Type: text/html\r\n\r\n")
        client.send(PAGE)
        client.close()
finally:
    robot.stopRobot()          # stop the wheels when the program ends
