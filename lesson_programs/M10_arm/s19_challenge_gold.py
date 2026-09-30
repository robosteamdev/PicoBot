from picobot_arm import PicoBotArm

arm = PicoBotArm()

while True:
    text = input("Channel 0, 1 or 2 (q = quit): ")
    if text == "q":
        break
    channel = int(text)
    angle = int(input("Angle: "))
    low = 40                    # arm and gripper
    high = 140
    if channel == 0:            # base
        low = 0
        high = 180
    safe = max(low, min(high, angle))
    print("Channel", channel, "->", safe, "degrees")
    arm.control_servo(channel, safe)

for channel in [0, 1, 2]:       # back home: 90, 90, 90
    arm.control_servo(channel, 90)
