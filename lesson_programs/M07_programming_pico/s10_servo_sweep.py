# Sweep the base servo slowly - inside the safe angles
from picobot_arm import PicoBotArm
import time

BASE = 0                                # channel 0 = base servo
MIN_ANGLE = {0: 0, 1: 40, 2: 40}        # safe limits (A1)
MAX_ANGLE = {0: 180, 1: 140, 2: 140}


def safe_angle(channel, angle):
    """Keep the angle inside the safe limits."""
    if angle < MIN_ANGLE[channel]:
        return MIN_ANGLE[channel]
    if angle > MAX_ANGLE[channel]:
        return MAX_ANGLE[channel]
    return angle


def pulse_ms(angle):
    return 0.5 + angle / 180 * 2.0


def move(channel, angle):
    angle = safe_angle(channel, angle)
    arm.control_servo(channel, angle)
    print(f"angle {angle:3d}   pulse {pulse_ms(angle):.2f} ms")
    time.sleep(0.1)


arm = PicoBotArm()          # all servos go to 90 degrees (home)
time.sleep(1)

for angle in range(90, 136, 5):     # 90 -> 135
    move(BASE, angle)
for angle in range(135, 44, -5):    # 135 -> 45
    move(BASE, angle)
for angle in range(45, 91, 5):      # 45 -> 90 (home)
    move(BASE, angle)
