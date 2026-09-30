# Turn one wheel of PicoBot: forward, then backward.
# The robot must be lifted: the wheels turn in the air!
from picobot_motors import MotorDriver
import time

motors = MotorDriver()      # talks to the motor driver board

print("Front-left wheel: forward")
motors.TurnMotor("LeftFront", "forward", 50)   # speed 50 %
time.sleep(2)               # let the wheel turn for 2 s

motors.MotorStop("LeftFront")                  # speed 0
time.sleep(0.5)             # short pause before we reverse

print("Front-left wheel: backward")
motors.TurnMotor("LeftFront", "backward", 50)
time.sleep(2)

motors.MotorStop("LeftFront")
print("Done")
