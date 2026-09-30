# Line follower: search a lost line, stop on the marker
from machine import Pin
import time
import picobot_motors

motors = picobot_motors.MotorDriver()

PINS = [8, 9, 13, 14, 15]        # D1 ... D5 (right -> left)
WEIGHTS = [2, 1, 0, -1, -2]
sensors = []
for p in PINS:
    sensors.append(Pin(p, Pin.IN, Pin.PULL_UP))

SPEED = 30
TURN = 0.2
SEARCH_SPEED = 30
GRACE_MS = 800


def limit(speed):
    return max(0, min(100, speed))


def drive(left_speed, right_speed):
    left_speed = limit(left_speed)
    right_speed = limit(right_speed)
    motors.TurnMotor('LeftFront', 'forward', left_speed)
    motors.TurnMotor('LeftBack', 'forward', left_speed)
    motors.TurnMotor('RightFront', 'forward', right_speed)
    motors.TurnMotor('RightBack', 'forward', right_speed)


def rotate(direction, speed):
    """Turn on the spot: direction 'right' or 'left'."""
    if direction == 'right':
        left_dir, right_dir = 'forward', 'backward'
    else:
        left_dir, right_dir = 'backward', 'forward'
    motors.TurnMotor('LeftFront', left_dir, speed)
    motors.TurnMotor('LeftBack', left_dir, speed)
    motors.TurnMotor('RightFront', right_dir, speed)
    motors.TurnMotor('RightBack', right_dir, speed)


def read_sensors():
    values = []
    for s in sensors:
        values.append(s.value())
    return values


def is_marker(values):
    return values == [1, 1, 1, 1, 1]


def line_position(values):
    total = 0
    count = 0
    for i in range(5):
        if values[i] == 1:
            total = total + WEIGHTS[i]
            count = count + 1
    if count == 0:
        return None
    return total / count


last_pos = 0
lost_since = None

try:
    while True:
        values = read_sensors()
        if is_marker(values):                   # 1. the marker?
            motors.StopAllMotors()
            print("Marker - stop!")
            break                               # end of the loop
        pos = line_position(values)
        if pos is not None:                     # 2. follow the line
            last_pos = pos
            lost_since = None
            left = round(SPEED * (1 + TURN * pos))
            right = round(SPEED * (1 - TURN * pos))
            drive(left, right)
        else:                                   # 3. search
            if lost_since is None:
                lost_since = time.ticks_ms()
            lost_ms = time.ticks_diff(time.ticks_ms(), lost_since)
            if lost_ms > GRACE_MS:
                motors.StopAllMotors()
            elif last_pos > 0:
                rotate('right', SEARCH_SPEED)
            elif last_pos < 0:
                rotate('left', SEARCH_SPEED)
            else:
                drive(SPEED, SPEED)
        time.sleep(0.01)
finally:
    motors.StopAllMotors()
