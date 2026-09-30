DEBOUNCE_MS = 1000     # ignore the marker for 1 s after a count

# (time in ms, do all 5 sensors see black?)
readings = [(0, False), (10, True), (20, True), (30, False),
            (40, True), (50, True), (60, False), (70, False),
            (2500, True), (2510, True), (2520, False)]

crossings = 0
on_marker = False
last_count_time = 0

for now, marker in readings:
    if marker and not on_marker:
        if crossings == 0 or now - last_count_time >= DEBOUNCE_MS:
            crossings = crossings + 1
            last_count_time = now
            print(now, "ms: crossing", crossings)
        else:
            print(now, "ms: flicker ignored")
    on_marker = marker

print("Crossings counted:", crossings)
