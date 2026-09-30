# Ramp the front-left wheel up and down (robot on the box!)
from picobot_motors import MotorDriver
import time

motors = MotorDriver()
WHEEL = "LeftFront"

try:
    for speed in range(0, 101, 10):      # 0, 10, 20 ... 100
        print("Speed:", speed)
        motors.TurnMotor(WHEEL, "forward", speed)
        time.sleep(1)
    for speed in range(90, -1, -10):     # 90, 80 ... 0
        print("Speed:", speed)
        motors.TurnMotor(WHEEL, "forward", speed)
        time.sleep(1)
finally:
    motors.StopAllMotors()               # ALWAYS stop the motors
    print("Motors stopped")
