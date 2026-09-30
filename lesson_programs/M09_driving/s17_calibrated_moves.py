# Moves in cm and degrees, using OUR calibration table.
from picobot import PicoBot
import time

SPEED = 50
CM_PER_S = 21.1         # forward speed (experiment 1)
SIDE_CM_PER_S = 17.0    # sideways speed (your measurement)
TIME_90 = 0.75          # seconds for 90 degrees (experiment 2)

robot = PicoBot()


def pause():
    robot.stopRobot()
    time.sleep(0.5)     # let the robot stand still


def forward_cm(cm):
    robot.goForward(SPEED)
    time.sleep(cm / CM_PER_S)
    pause()


def backward_cm(cm):
    robot.goBackward(SPEED)
    time.sleep(cm / CM_PER_S)
    pause()


def right_cm(cm):
    robot.moveRight(SPEED)
    time.sleep(cm / SIDE_CM_PER_S)
    pause()


def left_cm(cm):
    robot.moveLeft(SPEED)
    time.sleep(cm / SIDE_CM_PER_S)
    pause()


def turn_right(degrees):
    robot.rotateRight(SPEED)
    time.sleep(TIME_90 * degrees / 90)
    pause()


def turn_left(degrees):
    robot.rotateLeft(SPEED)
    time.sleep(TIME_90 * degrees / 90)
    pause()


# Test: a square with 40 cm sides, turning at each corner
for side in range(4):
    forward_cm(40)
    turn_right(90)
print("Square finished")
