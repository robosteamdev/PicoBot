# Turn around the front axle: the rear swings to the left.
from picobot import PicoBot
import time

robot = PicoBot()


def front_axle_right(speed=50):
    """Clockwise turn around the front axle."""
    robot.m.MotorStop("LeftFront")
    robot.m.MotorStop("RightFront")
    robot.m.TurnMotor("LeftBack", "forward", speed)
    robot.m.TurnMotor("RightBack", "backward", speed)


front_axle_right()
time.sleep(1)
robot.stopRobot()
