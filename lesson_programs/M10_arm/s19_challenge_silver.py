from picobot_arm import PicoBotArm
import time

arm = PicoBotArm()             # home: 90, 90, 90
time.sleep(1)

for clap in range(3):
    arm.control_servo(2, 60)   # gripper: 60 is inside 40-140
    time.sleep(0.5)
    arm.control_servo(2, 120)
    time.sleep(0.5)

arm.control_servo(2, 90)
