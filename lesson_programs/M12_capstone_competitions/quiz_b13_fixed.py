readings = [False, True, True, True, False, True, True, False]
crossings = 0
on_marker = False
for marker in readings:
    if marker and not on_marker:
        crossings = crossings + 1
    on_marker = marker
print("Crossings:", crossings)
