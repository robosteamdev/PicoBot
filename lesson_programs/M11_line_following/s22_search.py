# Proportional line follower that searches for a lost line
from machine import Pin
import time
import picobot_motors

motors = picobot_motors.MotorDriver()

PINS = [8, 9, 13, 14, 15]        # D1 ... D5 (right -> left)
WEIGHTS = [2, 1, 0, -1, -2]
sensors = []
for p in PINS:
    sensors.append(Pin(p, Pin.IN, Pin.PULL_UP))

SPEED = 30             # base speed in %
TURN = 0.2             # how strongly the robot steers
SEARCH_SPEED = 30      # turning speed while searching, in %
GRACE_MS = 800         # search at most 800 ms, then stop


def limit(speed):
    return max(0, min(100, speed))


def drive(left_speed, right_speed):
    left_speed = limit(left_speed)
    right_speed = limit(right_speed)
    motors.TurnMotor('LeftFront', 'forward', left_speed)
    motors.TurnMotor('LeftBack', 'forward', left_speed)
    motors.TurnMotor('RightFront', 'forward', right_speed)
    motors.TurnMotor('RightBack', 'forward', right_speed)


def rotate_right(speed):
    """Turn on the spot, clockwise."""
    motors.TurnMotor('LeftFront', 'forward', speed)
    motors.TurnMotor('LeftBack', 'forward', speed)
    motors.TurnMotor('RightFront', 'backward', speed)
    motors.TurnMotor('RightBack', 'backward', speed)


def rotate_left(speed):
    """Turn on the spot, counter-clockwise."""
    motors.TurnMotor('LeftFront', 'backward', speed)
    motors.TurnMotor('LeftBack', 'backward', speed)
    motors.TurnMotor('RightFront', 'forward', speed)
    motors.TurnMotor('RightBack', 'forward', speed)


def read_sensors():
    values = []
    for s in sensors:
        values.append(s.value())
    return values


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


last_pos = 0           # where the line was seen the last time
lost_since = None      # when the line was lost (None = not lost)

try:
    while True:
        pos = line_position(read_sensors())
        if pos is not None:                     # it sees the line
            last_pos = pos
            lost_since = None
            left = round(SPEED * (1 + TURN * pos))
            right = round(SPEED * (1 - TURN * pos))
            drive(left, right)
        else:                                   # the line is lost
            if lost_since is None:
                lost_since = time.ticks_ms()    # remember when
            lost_ms = time.ticks_diff(time.ticks_ms(), lost_since)
            if lost_ms > GRACE_MS:
                motors.StopAllMotors()          # give up: stop
            elif last_pos > 0:
                rotate_right(SEARCH_SPEED)      # it was on the right
            elif last_pos < 0:
                rotate_left(SEARCH_SPEED)       # it was on the left
            else:
                drive(SPEED, SPEED)             # it was in the middle
        time.sleep(0.01)
finally:
    motors.StopAllMotors()
