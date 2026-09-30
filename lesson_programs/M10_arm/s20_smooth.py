from picobot_arm import PicoBotArm
import time

arm = PicoBotArm()               # home: all servos at 90 degrees
time.sleep(1)

arm.smooth_move_servo(0, 45)     # base glides to 45 degrees
arm.smooth_move_servo(0, 135)    # ... then to 135 degrees
arm.smooth_move_servo(0, 90)     # ... and back to the middle

arm.control_servo(0, 45)         # compare: the base JUMPS to 45
time.sleep(1)
arm.control_servo(0, 90)         # and jumps back
print("Finished")
