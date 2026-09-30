# Lap counter logic - test it on the computer with a recorded run
MARKER_DEBOUNCE_MS = 1000
target_laps = 3

crossings = 0          # how many times the robot crossed the marker
laps_done = 0          # completed laps = crossings - 1
on_marker = False      # True while the sensors see the marker
last_marker_time = 0   # time (ms) of the last counted crossing


def ticks_diff(later, earlier):
    """On the Pico this is time.ticks_diff(). Here: a simple minus."""
    return later - earlier


def marker_seen(now):
    """Call when all 5 sensors see black.
    Returns True when the last lap is finished."""
    global crossings, laps_done, on_marker, last_marker_time
    if on_marker:
        return False               # still on the same marker
    on_marker = True
    passed = ticks_diff(now, last_marker_time)
    if crossings > 0 and passed < MARKER_DEBOUNCE_MS:
        print(now, "ms: flicker - ignored")
        return False
    crossings += 1
    last_marker_time = now
    laps_done = crossings - 1
    print(now, "ms: crossing", crossings, "- laps done:", laps_done)
    return laps_done >= target_laps


def marker_left():
    """Call when the sensors do not see the marker."""
    global on_marker
    on_marker = False


# Recorded run: (time in ms, do all 5 sensors see black?)
run = [(500, True), (560, True), (620, False), (650, True),
       (700, False), (8600, True), (8660, False), (16700, True),
       (16760, False), (24800, True), (24860, True)]

for now, marker in run:
    if marker:
        if marker_seen(now):
            print(now, "ms: STOP on the marker -", laps_done, "laps")
            break
    else:
        marker_left()
