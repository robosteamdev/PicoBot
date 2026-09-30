# Emergency stop: switch off all four wheel motors.
from picobot_motors import MotorDriver

motors = MotorDriver()
motors.StopAllMotors()
print("All motors stopped")
