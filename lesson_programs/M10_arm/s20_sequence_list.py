from picobot_arm import PicoBotArm
import time

arm = PicoBotArm()
time.sleep(1)

# (channel, angle): 0 = base, 1 = arm, 2 = gripper
steps = [(1, 100), (0, 45), (2, 120), (1, 70), (2, 60), (1, 100),
         (0, 135), (1, 70), (2, 120), (1, 100)]

for channel, angle in steps:
    print("channel", channel, "->", angle)
    arm.smooth_move_servo(channel, angle)
    time.sleep(0.3)

arm.reset_servos()
