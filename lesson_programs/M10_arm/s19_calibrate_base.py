from picobot_arm import PicoBotArm

arm = PicoBotArm()                    # home: 90, 90, 90

for angle in [0, 45, 90, 135, 180]:
    arm.control_servo(0, angle)       # base servo (channel 0)
    input(f"Base at {angle} degrees - measure, then press Enter ")

arm.control_servo(0, 90)              # back to the middle
print("Calibration finished")
