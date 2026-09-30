# Angle -> PCA9685 value -> pulse width, as in picobot_arm.py
MIN_PULSE = 102     # value for 0 degrees (about 0.5 ms)
MAX_PULSE = 512     # value for 180 degrees (about 2.5 ms)

print("angle  value  pulse")
for angle in range(0, 181, 45):
    value = int(MIN_PULSE + (angle / 180) * (MAX_PULSE - MIN_PULSE))
    pulse_ms = value / 4096 * 20        # 4096 steps in 20 ms
    print(f"{angle:5}  {value:5}  {pulse_ms:.2f} ms")
