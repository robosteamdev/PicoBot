from picobot_arm import PicoBotArm     # the arm library (file picobot_arm.py)
import time

arm = PicoBotArm()         # set up the servo driver; all servos go to 90 degrees
print("Arm at home: 90, 90, 90")
time.sleep(1)

arm.control_servo(0, 45)   # base (channel 0) to 45 degrees
time.sleep(1)              # give the servo time to get there
arm.control_servo(0, 135)  # base to 135 degrees
time.sleep(1)
arm.control_servo(0, 90)   # base back to the middle
print("Finished")
