# Wheel test: every wheel turns forward, then backward.
# The robot must be lifted!
from picobot_motors import MotorDriver
import time

motors = MotorDriver()
wheels = ["LeftFront", "RightFront", "LeftBack", "RightBack"]
SPEED = 50

for wheel in wheels:
    print(wheel, "forward")
    motors.TurnMotor(wheel, "forward", SPEED)
    time.sleep(1)
    motors.MotorStop(wheel)
    time.sleep(0.5)

    print(wheel, "backward")
    motors.TurnMotor(wheel, "backward", SPEED)
    time.sleep(1)
    motors.MotorStop(wheel)
    time.sleep(0.5)

motors.StopAllMotors()
print("Wheel test finished")
