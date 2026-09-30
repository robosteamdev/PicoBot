# How long can the robot drive? (example values, not measured)
CAPACITY_AH = 3.0       # 3000 mAh cells
USABLE = 0.8            # we stop at 7.0 V: only part is used (a guess)

for current in [0.5, 1.0, 1.5]:                 # average A
    hours = CAPACITY_AH * USABLE / current
    print(f"Average {current} A -> about {hours * 60:.0f} minutes")
