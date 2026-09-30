# Competition template: your task + START/STOP from the
# competition library.
import time
from machine import Pin
from picobot_motors import MotorDriver
from competition import Competition
import credentials as c      # settings from the organiser

motors = MotorDriver()
led = Pin("LED", Pin.OUT)

# Line sensor D1-D5 (right -> left), 1 = sees the line
sensors = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (8, 9, 13, 14, 15)]

SPEED = 30       # your tuned speed from module M11
LOOP_MS = 20     # call poll() every 20-50 ms


def set_wheels(left, right):
    """Forward speeds 0-100 for the left and right side."""
    motors.TurnMotor("LeftFront", "forward", left)
    motors.TurnMotor("LeftBack", "forward", left)
    motors.TurnMotor("RightFront", "forward", right)
    motors.TurnMotor("RightBack", "forward", right)


def drive_step():
    """ONE short step of your task. Replace it with your own
    line follower or lap counter from module M11."""
    right, rmid, centre, lmid, left = [s.value() for s in sensors]
    if left or lmid:
        set_wheels(SPEED // 2, SPEED)    # line on the left
    elif right or rmid:
        set_wheels(SPEED, SPEED // 2)    # line on the right
    else:
        set_wheels(SPEED, SPEED)         # centre: straight on


def when_start(run_id):      # the library gives the run number
    led.on()
    print("START, run", run_id)


def when_stop(run_id):
    motors.StopAllMotors()   # stop the wheels FIRST
    led.off()
    print("STOP, reason:", comp.stop_reason)


comp = Competition(
    ssid=c.WIFI_SSID, password=c.WIFI_PASSWORD,
    broker=c.MQTT_BROKER, port=c.MQTT_PORT,
    mqtt_user=c.MQTT_USER, mqtt_password=c.MQTT_PASSWORD,
    competition_id=c.COMPETITION_ID,
    friendly_name="Blue Sharks",   # your team name for the judges
)
comp.on_start(when_start)
comp.on_stop(when_stop)
comp.connect()
print("MAC address of this robot:", comp.mac)

driving = False
try:
    while True:
        comp.poll()              # check for START / STOP
        if comp.running:
            drive_step()
            driving = True
        elif driving:            # STOP came - or the network was lost
            motors.StopAllMotors()
            led.off()
            driving = False
        time.sleep_ms(LOOP_MS)
finally:
    motors.StopAllMotors()       # also when you press Stop
