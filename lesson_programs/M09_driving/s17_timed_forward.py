# Experiment: drive forward for a set time, then stop.
from picobot import PicoBot
import time

SPEED = 50          # speed value 0-100
DRIVE_TIME = 2.0    # seconds - change this: 1.0, 2.0, 3.0

robot = PicoBot()

for count in range(3, 0, -1):     # 3 s to put the robot down
    print("Start in", count)
    time.sleep(1)

robot.goForward(SPEED)
time.sleep(DRIVE_TIME)
robot.stopRobot()
print("Measure now!")
