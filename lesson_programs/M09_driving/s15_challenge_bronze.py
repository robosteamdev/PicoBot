from picobot_motors import MotorDriver
import time

motors = MotorDriver()
clockwise = ["LeftFront", "RightFront", "RightBack", "LeftBack"]

for wheel in clockwise:
    motors.TurnMotor(wheel, "forward", 50)
    time.sleep(1)
    motors.MotorStop(wheel)

motors.StopAllMotors()
