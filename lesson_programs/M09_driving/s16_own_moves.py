# The two missing moves of the movement chart.
from picobot import PicoBot
import time

robot = PicoBot()


def curve_right(speed=50):
    """Forward in a curve to the right: left wheels faster."""
    slow = speed // 2
    robot.m.TurnMotor("LeftFront", "forward", speed)
    robot.m.TurnMotor("LeftBack", "forward", speed)
    robot.m.TurnMotor("RightFront", "forward", slow)
    robot.m.TurnMotor("RightBack", "forward", slow)


def rear_axle_right(speed=50):
    """Turn around the rear axle: the front swings right."""
    robot.m.TurnMotor("LeftFront", "forward", speed)
    robot.m.TurnMotor("RightFront", "backward", speed)
    robot.m.MotorStop("LeftBack")
    robot.m.MotorStop("RightBack")


def drive(move, seconds, speed=50):
    """Start a move, wait, stop, pause."""
    move(speed)
    time.sleep(seconds)
    robot.stopRobot()
    time.sleep(1)


drive(curve_right, 2)
drive(rear_axle_right, 1)
print("Finished")
