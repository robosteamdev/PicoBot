from machine import Pin          # module of MicroPython for the Pico's pins
from picobot import PicoBot      # the PicoBot library (the file picobot.py on the robot)
import time

robot = PicoBot()
robot.goForward()                # function with a default speed of 50
time.sleep(2)
robot.stopRobot()
