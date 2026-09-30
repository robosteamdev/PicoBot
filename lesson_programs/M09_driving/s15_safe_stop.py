# Runs until you click Stop - and then stops the motors.
from picobot_motors import MotorDriver
import time

motors = MotorDriver()

try:
    while True:                   # repeat until Stop
        motors.TurnMotor("RightBack", "forward", 40)
        time.sleep(1)
        motors.MotorStop("RightBack")
        time.sleep(0.5)
        motors.TurnMotor("RightBack", "backward", 40)
        time.sleep(1)
        motors.MotorStop("RightBack")
        time.sleep(0.5)
finally:
    motors.StopAllMotors()        # runs also after Stop
    print("Motors stopped")
