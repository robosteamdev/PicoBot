# Two crossings of the marker, one value every 10 ms
readings = [False, False, True, True, True, True, True, False,
            False, False, True, True, True, False]

crossings = 0
on_marker = False              # state variable: on the marker now?

for marker in readings:
    if marker and not on_marker:        # we just arrived
        crossings = crossings + 1
        print("Crossing", crossings)
    on_marker = marker                  # remember for the next pass

print("Crossings counted:", crossings)
