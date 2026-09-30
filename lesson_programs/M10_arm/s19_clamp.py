# Keep an angle between two limits ("clamp" it).
MIN_ARM = 40       # safe limits of the arm servo (channel 1)
MAX_ARM = 140

for wanted in [150, 20, 100]:
    safe = max(MIN_ARM, min(MAX_ARM, wanted))
    print("wanted", wanted, "-> safe", safe)
