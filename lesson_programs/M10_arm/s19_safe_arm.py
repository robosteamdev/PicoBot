from picobot_arm import PicoBotArm
import time

MIN_ARM = 40       # safe limits of the arm servo (channel 1)
MAX_ARM = 140

arm = PicoBotArm()          # home: all servos to 90 degrees
time.sleep(1)

wanted = 150                # try 150, 20, 120 ...
safe = max(MIN_ARM, min(MAX_ARM, wanted))
print("wanted", wanted, "- the arm goes to", safe)
arm.control_servo(1, safe)  # arm servo (channel 1)
time.sleep(2)
arm.control_servo(1, 90)    # back to home
