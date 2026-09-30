# Final mini-challenge: follow the line, stop on the marker,
# pick up the cube and put it on the target.
from machine import Pin
import time
import picobot_motors
from picobot_arm import PicoBotArm

motors = picobot_motors.MotorDriver()
arm = PicoBotArm()               # the arm goes home: 90, 90, 90
time.sleep(1)

# ---- Line follower: settings from session 9 ----
PINS = [8, 9, 13, 14, 15]        # D1 ... D5 (right -> left)
WEIGHTS = [2, 1, 0, -1, -2]
SPEED = 30
TURN = 0.2
SEARCH_SPEED = 30
GRACE_MS = 800

# ---- Arm: angles taught at the REAL stop position ----
BASE_PICK = 45       # base turned to the pick zone
BASE_PLACE = 135     # base turned to the target
ARM_DOWN = 70        # gripper at the height of the cube
ARM_CARRY = 100      # arm lifted to carry the cube
GRIP_OPEN = 120      # gripper open
GRIP_CLOSED = 60     # gripper just holds the cube

sensors = []
for p in PINS:
    sensors.append(Pin(p, Pin.IN, Pin.PULL_UP))


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


def follow_to_marker():
    """Step 1. True = marker reached, False = line lost."""
    last_pos = 0
    lost_since = None
    while True:
        values = read_sensors()
        if is_marker(values):
            motors.StopAllMotors()
            return True
        pos = line_position(values)
        if pos is not None:
            last_pos = pos
            lost_since = None
            left = round(SPEED * (1 + TURN * pos))
            right = round(SPEED * (1 - TURN * pos))
            drive(left, right)
        else:
            if lost_since is None:
                lost_since = time.ticks_ms()
            lost_ms = time.ticks_diff(time.ticks_ms(), lost_since)
            if lost_ms > GRACE_MS:
                motors.StopAllMotors()
                return False
            elif last_pos > 0:
                rotate('right', SEARCH_SPEED)
            elif last_pos < 0:
                rotate('left', SEARCH_SPEED)
            else:
                drive(SPEED, SPEED)
        time.sleep(0.01)


def move(channel, angle):
    """Move one servo smoothly, never outside its safe limits."""
    low = 40                  # arm and gripper: 40-140 degrees
    high = 140
    if channel == 0:          # base: 0-180 degrees
        low = 0
        high = 180
    angle = max(low, min(high, angle))
    arm.smooth_move_servo(channel, angle)
    time.sleep(0.3)           # let the servo settle


def pick(base_angle):
    """Step 2."""
    move(1, ARM_CARRY)        # arm up, so it does not hit anything
    move(0, base_angle)       # turn to the cube
    move(2, GRIP_OPEN)        # open the gripper
    move(1, ARM_DOWN)         # lower the gripper around the cube
    move(2, GRIP_CLOSED)      # close: hold the cube
    move(1, ARM_CARRY)        # lift the cube


def place(base_angle):
    """Step 3."""
    move(0, base_angle)       # turn to the target
    move(1, ARM_DOWN)         # lower the cube
    move(2, GRIP_OPEN)        # let go
    move(1, ARM_CARRY)        # lift the empty gripper


# ---- The mission ----
try:
    if follow_to_marker():
        print("Step 1 done: on the marker")
        time.sleep(0.5)       # wait until the robot stands still
        pick(BASE_PICK)
        print("Step 2 done: cube lifted")
        place(BASE_PLACE)
        arm.reset_servos()    # smoothly back home
        print("Step 3 done: mission complete")
    else:
        print("Line lost - mission stopped")
finally:
    motors.StopAllMotors()
