# Capstone A: the mission as a state machine with a step table
# BOOTSEL = START, press again = STOP. Non-blocking: no sleep()
# longer than 20 ms, so STOP works in every state.
import time
import rp2
from machine import Pin
from picobot_motors import MotorDriver
from picobot_arm import PicoBotArm

motors = MotorDriver()
arm = PicoBotArm()            # all servos to 90 degrees (home)
sensors = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (8, 9, 13, 14, 15)]

SPEED = 30                    # line-following speed
BASE, ARM, GRIP = 0, 1, 2     # servo channels

# The step table: (kind, value 1, value 2, wait in ms)
STEPS = [
    ("servo", BASE, 45, 600),     # base 45 deg to one side
    ("servo", GRIP, 60, 600),     # close the gripper
    ("servo", ARM, 100, 600),     # lift (carry angle)
    ("servo", BASE, 135, 600),    # base 45 deg to the other side
    ("servo", ARM, 70, 600),      # lower
    ("servo", GRIP, 120, 600),    # release
    ("servo", ARM, 100, 600),     # transport position
    ("back", 35, 0, 600),         # back about 10 cm - TUNE
    ("turn", 40, 0, 1000),        # turn about 180 deg - TUNE
]


def set_wheels(left, right):
    """Speeds -100..100: minus = backward."""
    for name, speed in (("LeftFront", left), ("LeftBack", left),
                        ("RightFront", right), ("RightBack", right)):
        direction = "forward" if speed >= 0 else "backward"
        motors.TurnMotor(name, direction, abs(speed))


def start_step(kind, a, b):
    if kind == "servo":
        arm.control_servo(a, b)       # a = channel, b = angle
    elif kind == "back":
        set_wheels(-a, -a)            # a = speed
    elif kind == "turn":
        set_wheels(-a, a)             # rotate left on the spot


def follow_line():
    """One step of line following. True = on a marker."""
    r, rm, c, lm, l = [s.value() for s in sensors]
    if r and rm and c and lm and l:
        motors.StopAllMotors()
        return True
    if l or lm:
        set_wheels(SPEED // 2, SPEED)
    elif r or rm:
        set_wheels(SPEED, SPEED // 2)
    else:
        set_wheels(SPEED, SPEED)
    return False


state = "IDLE"
step = 0
step_start = 0
was_pressed = False


def change(new_state):
    global state, step, step_start
    print(state, "->", new_state)
    state = new_state
    step = 0
    step_start = time.ticks_ms()


try:
    while True:
        now = time.ticks_ms()
        pressed = rp2.bootsel_button() == 1
        new_press = pressed and not was_pressed
        was_pressed = pressed

        if new_press and state != "IDLE":
            motors.StopAllMotors()        # STOP in any state
            change("IDLE")
        elif state == "IDLE":
            if new_press:                 # START
                arm.control_servo(BASE, 90)
                arm.control_servo(ARM, 100)
                arm.control_servo(GRIP, 120)
                change("OUTBOUND")
        elif state == "OUTBOUND":
            if follow_line():
                change("ARM_SEQ")
                start_step(*STEPS[0][:3])
        elif state == "ARM_SEQ":
            if time.ticks_diff(now, step_start) >= STEPS[step][3]:
                motors.StopAllMotors()    # end of a drive step
                step += 1
                step_start = now
                if step < len(STEPS):
                    start_step(*STEPS[step][:3])
                else:
                    change("RETURNING")
        elif state == "RETURNING":
            if follow_line():
                change("DONE")
        time.sleep_ms(20)
finally:
    motors.StopAllMotors()
