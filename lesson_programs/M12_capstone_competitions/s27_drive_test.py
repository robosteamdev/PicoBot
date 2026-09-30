# Calibration run: drive back or turn for a set time.
# The robot is on the floor. Measure the result after the run.
import time
from picobot_motors import MotorDriver

MODE = "back"       # "back" or "turn"
SPEED = 35          # mission: back 35, turn 40
TIME_MS = 600       # mission: back 600, turn 1000

motors = MotorDriver()


def set_wheels(left, right):
    """Speeds -100..100: minus = backward."""
    for name, speed in (("LeftFront", left), ("LeftBack", left),
                        ("RightFront", right), ("RightBack", right)):
        direction = "forward" if speed >= 0 else "backward"
        motors.TurnMotor(name, direction, abs(speed))


print("Start in 3 s - hands away!")
time.sleep(3)
if MODE == "back":
    set_wheels(-SPEED, -SPEED)      # all wheels backward
else:
    set_wheels(-SPEED, SPEED)       # rotate left on the spot
time.sleep_ms(TIME_MS)
motors.StopAllMotors()
print("Done:", MODE, "speed", SPEED, "for", TIME_MS, "ms")
