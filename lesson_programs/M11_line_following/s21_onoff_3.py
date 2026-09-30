# On/off line follower with 3 sensors (D2, D3, D4)
from machine import Pin
import time
import picobot_motors

motors = picobot_motors.MotorDriver()

right_mid = Pin(9, Pin.IN, Pin.PULL_UP)     # D2
centre = Pin(13, Pin.IN, Pin.PULL_UP)       # D3
left_mid = Pin(14, Pin.IN, Pin.PULL_UP)     # D4

SPEED = 30          # speed in % (0-100) - start slowly!


def drive(left_speed, right_speed):
    """Left wheels and right wheels forward, speed 0-100 %."""
    motors.TurnMotor('LeftFront', 'forward', left_speed)
    motors.TurnMotor('LeftBack', 'forward', left_speed)
    motors.TurnMotor('RightFront', 'forward', right_speed)
    motors.TurnMotor('RightBack', 'forward', right_speed)


try:
    while True:
        if centre.value() == 1:         # line in the middle
            drive(SPEED, SPEED)         # straight on
        elif right_mid.value() == 1:    # line on the right
            drive(SPEED, 0)             # turn right
        elif left_mid.value() == 1:     # line on the left
            drive(0, SPEED)             # turn left
        else:                           # no sensor sees the line
            motors.StopAllMotors()
        time.sleep(0.01)                # wait 10 ms, then again
finally:
    motors.StopAllMotors()              # always stop at the end
