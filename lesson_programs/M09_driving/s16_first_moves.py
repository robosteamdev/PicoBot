# First moves with the PicoBot class.
from picobot import PicoBot
import time

robot = PicoBot()       # wheels + arm (the arm moves to 90 degrees)

robot.goForward()       # all four wheels forward, speed 50
time.sleep(1)
robot.stopRobot()       # stop all wheels
time.sleep(1)

robot.goBackward(70)    # backward, speed 70
time.sleep(1)
robot.stopRobot()
print("Finished")
