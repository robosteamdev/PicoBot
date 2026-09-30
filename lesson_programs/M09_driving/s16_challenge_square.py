from picobot import PicoBot
import time

robot = PicoBot()


def drive(move, seconds, speed=50):
    move(speed)
    time.sleep(seconds)
    robot.stopRobot()
    time.sleep(0.5)


for move in [robot.goForward, robot.moveRight,
             robot.goBackward, robot.moveLeft]:
    drive(move, 1)
