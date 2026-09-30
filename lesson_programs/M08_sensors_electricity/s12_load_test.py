# Load test: read the battery voltage without and with load
# The robot must be LIFTED: the wheels turn in the air!
from picobot_motors import MotorDriver
import time

motors = MotorDriver()
WHEELS = ["LeftFront", "LeftBack", "RightFront", "RightBack"]

try:
    print("No load: read the voltage now (5 s)")
    time.sleep(5)
    for w in WHEELS:
        motors.TurnMotor(w, "forward", speed=60)
    print("All wheels running: read the voltage now (3 s)")
    time.sleep(3)
finally:
    motors.StopAllMotors()      # always stop the wheels at the end
    print("Stopped: read the voltage again")
