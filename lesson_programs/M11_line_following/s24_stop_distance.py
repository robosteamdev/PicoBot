# Drive forward and stop in front of an obstacle
from machine import Pin, time_pulse_us
import time
import picobot_motors

motors = picobot_motors.MotorDriver()
trig = Pin(27, Pin.OUT, value=0)
echo = Pin(26, Pin.IN)

SPEED = 30
STOP_CM = 20        # stop when an obstacle is closer than this


def distance_cm():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    t = time_pulse_us(echo, 1, 30000)
    if t < 0:
        return 999
    return t * 0.0343 / 2


def forward(speed):
    for m in ['LeftFront', 'LeftBack', 'RightFront', 'RightBack']:
        motors.TurnMotor(m, 'forward', speed)


try:
    forward(SPEED)
    while distance_cm() >= STOP_CM:     # the way is free
        time.sleep(0.02)
    motors.StopAllMotors()
    time.sleep(1)                       # wait until it stands still
    print("Distance after the stop:", round(distance_cm(), 1), "cm")
finally:
    motors.StopAllMotors()
