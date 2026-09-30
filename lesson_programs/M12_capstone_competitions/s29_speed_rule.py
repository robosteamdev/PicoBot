# Faster on the straight parts: test the rule on the computer
NORMAL = 30          # speed in curves
FAST = 45            # speed on straight parts
STRAIGHT_MS = 300    # line in the middle this long = straight
LOOP_MS = 50         # one pass of the loop (simulated)


def choose_speed(pos, straight_ms):
    """Speed for the line position pos (0 = middle)."""
    if pos == 0 and straight_ms >= STRAIGHT_MS:
        return FAST
    return NORMAL


# Recorded line positions, one every 50 ms
positions = [0, 0, 0, 0, 0, 0, 0, 0.5, 1, 1.5, 0, 0]

straight_ms = 0
for i in range(len(positions)):
    pos = positions[i]
    if pos == 0:
        straight_ms = straight_ms + LOOP_MS
    else:
        straight_ms = 0          # a curve: start again
    speed = choose_speed(pos, straight_ms)
    print(f"{i * LOOP_MS:4} ms  pos {pos:4}  speed {speed}")
