from picobot_arm import PicoBotArm
import time

BASE_A = 45
ARM_DOWN = 70
ARM_CARRY = 100
GRIP_OPEN = 120
GRIP_CLOSED = 60

arm = PicoBotArm()
time.sleep(1)

arm.smooth_move_servo(1, ARM_CARRY)     # arm up
arm.smooth_move_servo(0, BASE_A)        # turn to spot A
arm.smooth_move_servo(2, GRIP_OPEN)
arm.smooth_move_servo(1, ARM_DOWN)
arm.smooth_move_servo(2, GRIP_CLOSED)   # hold the cube
arm.smooth_move_servo(1, ARM_CARRY)     # lift it
time.sleep(2)                           # hold for 2 seconds
arm.smooth_move_servo(1, ARM_DOWN)      # put it back
arm.smooth_move_servo(2, GRIP_OPEN)
arm.smooth_move_servo(1, ARM_CARRY)
arm.reset_servos()                      # home
