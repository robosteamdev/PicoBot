# Test the ten library moves, one after the other.
from picobot import PicoBot
import time

robot = PicoBot()


def drive(move, seconds, speed=50):
    """Start a move, wait, stop, pause."""
    move(speed)             # e.g. robot.goForward(50)
    time.sleep(seconds)
    robot.stopRobot()
    time.sleep(1)           # pause: look where the robot is


moves = [
    ("forward", robot.goForward),
    ("backward", robot.goBackward),
    ("sideways right", robot.moveRight),
    ("sideways left", robot.moveLeft),
    ("diagonal forward-right", robot.moveRightForward),
    ("diagonal backward-left", robot.moveLeftBackward),
    ("diagonal forward-left", robot.moveLeftForward),
    ("diagonal backward-right", robot.moveRightBackward),
    ("turn right", robot.rotateRight),
    ("turn left", robot.rotateLeft),
]

for name, move in moves:
    print("Next move:", name)
    drive(move, 1)

print("All moves done")
