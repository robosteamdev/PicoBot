readings = [False, True, True, True, False, True, True, False]
crossings = 0
for marker in readings:
    if marker:
        crossings = crossings + 1
print("Crossings:", crossings)
