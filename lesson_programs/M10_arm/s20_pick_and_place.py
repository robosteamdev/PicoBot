from picobot_arm import PicoBotArm
import time

# Angles found by teaching - change them for YOUR robot
BASE_A = 45          # base turned to spot A
BASE_B = 135         # base turned to target B
ARM_DOWN = 70        # gripper at the height of the cube
ARM_CARRY = 100      # arm lifted to carry the cube
GRIP_OPEN = 120      # gripper open
GRIP_CLOSED = 60     # gripper just holds the cube

arm = PicoBotArm()   # start at home: 90, 90, 90
time.sleep(1)


def move(channel, angle):
    """Move one servo smoothly, never outside its safe limits."""
    low = 40                  # arm and gripper: 40-140 degrees
    high = 140
    if channel == 0:          # base: 0-180 degrees
        low = 0
        high = 180
    angle = max(low, min(high, angle))
    arm.smooth_move_servo(channel, angle)
    time.sleep(0.3)           # let the servo settle


def pick(base_angle):
    move(1, ARM_CARRY)        # arm up, so it does not hit anything
    move(0, base_angle)       # turn to the cube
    move(2, GRIP_OPEN)        # open the gripper
    move(1, ARM_DOWN)         # lower the gripper around the cube
    move(2, GRIP_CLOSED)      # close: hold the cube
    move(1, ARM_CARRY)        # lift the cube


def place(base_angle):
    move(0, base_angle)       # turn to the target
    move(1, ARM_DOWN)         # lower the cube
    move(2, GRIP_OPEN)        # let go
    move(1, ARM_CARRY)        # lift the empty gripper


pick(BASE_A)
place(BASE_B)
arm.reset_servos()            # smoothly back home (90, 90, 90)
print("Cube moved from A to B")
