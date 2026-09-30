# Lap counter: follow the line, count the marker crossings,
# stop on the marker after target_laps laps.
# Start the robot on the line BEHIND the marker.
from machine import Pin
from time import sleep, ticks_ms, ticks_diff
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
MARKER_DEBOUNCE_MS = 1000
target_laps = 3

crossings = 0
laps_done = 0
on_marker = False
last_marker_time = 0
last_pos = 0
lost_since = None


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


def marker_seen(now):
    """Call when all 5 sensors see black.
    Returns True when the last lap is finished."""
    global crossings, laps_done, on_marker, last_marker_time
    if on_marker:
        return False
    on_marker = True
    passed = ticks_diff(now, last_marker_time)
    if crossings > 0 and passed < MARKER_DEBOUNCE_MS:
        return False
    crossings += 1
    last_marker_time = now
    laps_done = crossings - 1
    print("Crossing", crossings, "- laps done:", laps_done)
    return laps_done >= target_laps


def marker_left():
    global on_marker
    on_marker = False


def follow_line(values):
    """Proportional steering; search when the line is lost."""
    global last_pos, lost_since
    pos = line_position(values)
    if pos is not None:
        last_pos = pos
        lost_since = None
        drive(round(SPEED * (1 + TURN * pos)),
              round(SPEED * (1 - TURN * pos)))
        return
    if lost_since is None:
        lost_since = ticks_ms()
    if ticks_diff(ticks_ms(), lost_since) > GRACE_MS:
        motors.StopAllMotors()
    elif last_pos > 0:
        rotate('right', SEARCH_SPEED)
    elif last_pos < 0:
        rotate('left', SEARCH_SPEED)
    else:
        drive(SPEED, SPEED)


try:
    while True:
        values = read_sensors()
        if values == [1, 1, 1, 1, 1]:          # on the marker
            if marker_seen(ticks_ms()):         # last lap done?
                motors.StopAllMotors()
                print("Finished:", laps_done, "laps")
                break
            drive(SPEED, SPEED)                 # straight over it
        else:
            marker_left()
            follow_line(values)
        sleep(0.01)
finally:
    motors.StopAllMotors()
