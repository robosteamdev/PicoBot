distances = [45, 18, 60, 12, 30]    # cm
closest = distances[0]
too_close = 0
for d in distances:                 # no index needed
    if d < closest:
        closest = d
    if d < 20:
        too_close += 1              # not too_close++
print("Closest:", closest)
print("Too close:", too_close)
