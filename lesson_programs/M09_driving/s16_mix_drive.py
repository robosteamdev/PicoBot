# Drive any combination of forward, sideways and turning.
from picobot import PicoBot
import time

robot = PicoBot()
WHEELS = ["LeftFront", "RightFront", "LeftBack", "RightBack"]


def mix(forward, right, turn):
    fl = forward + right + turn
    fr = forward - right - turn
    bl = forward - right + turn
    br = forward + right - turn
    return [fl, fr, bl, br]


def drive_mix(forward, right, turn):
    values = mix(forward, right, turn)
    for i in range(4):
        speed = min(abs(values[i]), 100)    # 0 ... 100
        if values[i] >= 0:
            robot.m.TurnMotor(WHEELS[i], "forward", speed)
        else:
            robot.m.TurnMotor(WHEELS[i], "backward", speed)


drive_mix(30, 30, 0)        # diagonal forward-right
time.sleep(1)
robot.stopRobot()
time.sleep(1)
drive_mix(40, 0, 15)        # a wide curve to the right
time.sleep(2)
robot.stopRobot()
