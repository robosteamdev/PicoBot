# One crossing of the marker, one value every 10 ms:
# True = all 5 sensors see black
readings = [False, False, True, True, True, True, True, False, False]

crossings = 0
for marker in readings:
    if marker:
        crossings = crossings + 1

print("Crossings counted:", crossings)
