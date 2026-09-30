# Find the smallest speed at which a wheel turns.
# The robot must be lifted!
from picobot_motors import MotorDriver
import time

motors = MotorDriver()
WHEEL = "LeftFront"

for speed in range(0, 101, 5):      # 0, 5, 10 ... 100
    print("speed", speed)
    motors.TurnMotor(WHEEL, "forward", speed)
    time.sleep(1.5)

motors.StopAllMotors()
print("Finished")
