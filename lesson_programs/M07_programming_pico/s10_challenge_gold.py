from picobot_motors import MotorDriver
import time

motors = MotorDriver()

try:
    for speed in [30, 50, 70, 100]:
        motors.TurnMotor("LeftFront", "forward", speed)
        print("Speed", speed, "- start counting in 2 s")
        time.sleep(2)                   # let the wheel reach its speed
        print("COUNT NOW for 10 s")
        time.sleep(10)
        print("STOP counting")
finally:
    motors.StopAllMotors()
