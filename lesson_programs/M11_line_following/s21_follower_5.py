# Proportional line follower with 5 sensors
from machine import Pin
import time
import picobot_motors

motors = picobot_motors.MotorDriver()

PINS = [8, 9, 13, 14, 15]        # D1 ... D5 (right -> left)
WEIGHTS = [2, 1, 0, -1, -2]
sensors = []
for p in PINS:
    sensors.append(Pin(p, Pin.IN, Pin.PULL_UP))

SPEED = 30       # base speed in %
TURN = 0.2       # how strongly the robot steers


def limit(speed):
    """Keep a speed between 0 and 100 %."""
    return max(0, min(100, speed))


def drive(left_speed, right_speed):
    left_speed = limit(left_speed)
    right_speed = limit(right_speed)
    motors.TurnMotor('LeftFront', 'forward', left_speed)
    motors.TurnMotor('LeftBack', 'forward', left_speed)
    motors.TurnMotor('RightFront', 'forward', right_speed)
    motors.TurnMotor('RightBack', 'forward', right_speed)


def line_position():
    """Weighted position of the line, or None if it is lost."""
    total = 0
    count = 0
    for i in range(5):
        if sensors[i].value() == 1:
            total = total + WEIGHTS[i]
            count = count + 1
    if count == 0:
        return None
    return total / count


try:
    while True:
        pos = line_position()
        if pos is None:                 # line lost: stop
            motors.StopAllMotors()
        else:
            left = round(SPEED * (1 + TURN * pos))
            right = round(SPEED * (1 - TURN * pos))
            drive(left, right)
        time.sleep(0.01)
finally:
    motors.StopAllMotors()
