from picobot_arm import PicoBotArm
import time

arm = PicoBotArm()                         # home: 90, 90, 90
time.sleep(1)

for step in [1, 2, 5]:
    start = time.ticks_ms()                # time before the move
    arm.smooth_move_servo(0, 135, step)    # base: 90 -> 135
    ms = time.ticks_diff(time.ticks_ms(), start)
    print("step", step, ":", ms, "ms")
    arm.smooth_move_servo(0, 90)           # back to the middle
    time.sleep(0.5)
