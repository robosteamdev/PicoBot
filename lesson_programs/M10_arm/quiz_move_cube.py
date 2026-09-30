from picobot_arm import PicoBotArm
import time

BASE_A = 45
BASE_B = 135
ARM_DOWN = 70
ARM_CARRY = 100
GRIP_OPEN = 120
GRIP_CLOSED = 60

arm = PicoBotArm()                     # home: 90, 90, 90
time.sleep(1)

steps = [(1, ARM_CARRY), (0, BASE_A), (2, GRIP_OPEN), (1, ARM_DOWN),
         (2, GRIP_CLOSED), (1, ARM_CARRY), (0, BASE_B), (1, ARM_DOWN),
         (2, GRIP_OPEN), (1, ARM_CARRY)]

for channel, angle in steps:
    low = 40                           # arm and gripper
    high = 140
    if channel == 0:                   # base
        low = 0
        high = 180
    arm.smooth_move_servo(channel, max(low, min(high, angle)))
    time.sleep(0.3)

arm.reset_servos()                     # home
