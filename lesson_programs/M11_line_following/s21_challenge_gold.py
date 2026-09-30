# On/off line follower with all 5 sensors
from machine import Pin
import time
import picobot_motors

motors = picobot_motors.MotorDriver()

d1 = Pin(8, Pin.IN, Pin.PULL_UP)      # right
d2 = Pin(9, Pin.IN, Pin.PULL_UP)      # right-middle
d3 = Pin(13, Pin.IN, Pin.PULL_UP)     # centre
d4 = Pin(14, Pin.IN, Pin.PULL_UP)     # left-middle
d5 = Pin(15, Pin.IN, Pin.PULL_UP)     # left

SPEED = 30


def drive(left_speed, right_speed):
    motors.TurnMotor('LeftFront', 'forward', left_speed)
    motors.TurnMotor('LeftBack', 'forward', left_speed)
    motors.TurnMotor('RightFront', 'forward', right_speed)
    motors.TurnMotor('RightBack', 'forward', right_speed)


try:
    while True:
        if d3.value() == 1:
            drive(SPEED, SPEED)             # straight on
        elif d2.value() == 1:
            drive(SPEED, SPEED // 2)        # gentle right
        elif d1.value() == 1:
            drive(SPEED, 0)                 # sharp right
        elif d4.value() == 1:
            drive(SPEED // 2, SPEED)        # gentle left
        elif d5.value() == 1:
            drive(0, SPEED)                 # sharp left
        else:
            motors.StopAllMotors()          # line lost
        time.sleep(0.01)
finally:
    motors.StopAllMotors()
