# Drive forward and strafe around obstacles - a state machine
from machine import Pin, time_pulse_us
import time
import picobot_motors

motors = picobot_motors.MotorDriver()
trig = Pin(27, Pin.OUT, value=0)
echo = Pin(26, Pin.IN)

SPEED = 40
AVOID_CM = 15          # obstacle closer than this: strafe
STRAFE_MS = 1300       # strafe at least this long
NUM_OBSTACLES = 3      # how many obstacles, then finish
FINISH_MS = 1000       # drive on this long after the last one


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


def strafe_left(speed):
    """Sideways to the left, like robot.moveLeft()."""
    motors.TurnMotor('LeftFront', 'backward', speed)
    motors.TurnMotor('LeftBack', 'forward', speed)
    motors.TurnMotor('RightFront', 'forward', speed)
    motors.TurnMotor('RightBack', 'backward', speed)


def strafe_right(speed):
    """Sideways to the right, like robot.moveRight()."""
    motors.TurnMotor('LeftFront', 'forward', speed)
    motors.TurnMotor('LeftBack', 'backward', speed)
    motors.TurnMotor('RightFront', 'backward', speed)
    motors.TurnMotor('RightBack', 'forward', speed)


state = "FORWARD"
since = time.ticks_ms()        # when the state started
cleared = 0                    # obstacles passed

try:
    while state != "DONE":
        d = distance_cm()
        now = time.ticks_ms()
        in_state_ms = time.ticks_diff(now, since)

        if state == "FORWARD":
            forward(SPEED)
            if d < AVOID_CM:
                if cleared % 2 == 0:
                    state = "STRAFE_LEFT"
                else:
                    state = "STRAFE_RIGHT"
                since = now
                print(state, "- obstacle at", round(d), "cm")

        elif state == "STRAFE_LEFT" or state == "STRAFE_RIGHT":
            if state == "STRAFE_LEFT":
                strafe_left(SPEED)
            else:
                strafe_right(SPEED)
            if d >= AVOID_CM and in_state_ms >= STRAFE_MS:
                cleared = cleared + 1
                if cleared >= NUM_OBSTACLES:
                    state = "FINISH"
                else:
                    state = "FORWARD"
                since = now
                print(state, "- obstacles cleared:", cleared)

        elif state == "FINISH":
            forward(SPEED)
            if in_state_ms >= FINISH_MS:
                state = "DONE"

        time.sleep(0.05)               # 50 ms, like the ready program
finally:
    motors.StopAllMotors()
    print("DONE")
