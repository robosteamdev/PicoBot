from picobot_motors import MotorDriver
import time

motors = MotorDriver()

for speed in range(0, 101, 10):       # 0, 10 ... 100
    motors.TurnMotor("RightFront", "forward", speed)
    time.sleep(0.5)

for speed in range(100, -1, -10):     # 100, 90 ... 0
    motors.TurnMotor("RightFront", "forward", speed)
    time.sleep(0.5)

motors.StopAllMotors()
