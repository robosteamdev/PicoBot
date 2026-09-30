# Calibration: which time gives 10 cm back and 180 deg turn?
# Replace the example measurements with your own.


def time_for(target, tries):
    """tries: list of (time in ms, measured result).
    Assumes: result grows in proportion to the time."""
    rate = 0
    for time_ms, result in tries:
        rate = rate + result / time_ms    # result per ms
    rate = rate / len(tries)              # average
    return target / rate


# Drive back at speed 35: (time in ms, distance in cm)
back = [(600, 11.5), (600, 12.0), (600, 11.2)]
# Turn at speed 40: (time in ms, angle in degrees)
turn = [(1000, 205), (1000, 198), (1000, 211)]

print("Drive back 10 cm:", round(time_for(10, back)), "ms")
print("Turn 180 deg:", round(time_for(180, turn)), "ms")
