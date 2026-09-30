from picobot import PicoBot
import time

robot = PicoBot()


def drive(move, seconds):
    move()                  # start the move (speed 50)
    time.sleep(seconds)
    robot.stopRobot()
    time.sleep(0.5)


drive(robot.goForward, 2)
drive(robot.moveRight, 1)
drive(robot.goBackward, 2)
drive(robot.moveLeft, 1)
drive(robot.rotateRight, 1)
print("Finished")
