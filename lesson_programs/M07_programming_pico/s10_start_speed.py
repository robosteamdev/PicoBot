# At which speed does the wheel start to turn?
from picobot_motors import MotorDriver
import time

motors = MotorDriver()
WHEEL = "LeftFront"          # change: LeftBack, RightFront, RightBack

try:
    for speed in range(0, 62, 2):        # 0, 2, 4 ... 60
        print("Speed:", speed)
        motors.TurnMotor(WHEEL, "forward", speed)
        time.sleep(1.5)
finally:
    motors.StopAllMotors()
