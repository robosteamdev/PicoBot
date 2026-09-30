# The obstacle state machine - simulated on the computer
AVOID_CM = 10          # obstacle closer than this: strafe
STRAFE_MS = 1300       # strafe at least this long
NUM_OBSTACLES = 2
FINISH_MS = 1000       # drive on this long after the last one

# When does the sensor see an obstacle? (from ms, to ms)
OBSTACLE_TIMES = [(1000, 1500), (4000, 4800)]


def distance_at(t):
    for start, end in OBSTACLE_TIMES:
        if start <= t < end:
            return 8           # an obstacle 8 cm in front
    return 999                 # nothing in front


state = "FORWARD"
since = 0              # time when the state started
cleared = 0            # obstacles passed
print(0, "ms:", state)

for t in range(0, 8000, 50):           # one step every 50 ms
    d = distance_at(t)
    if state == "FORWARD":
        if d < AVOID_CM:
            if cleared % 2 == 0:       # 1st, 3rd ... obstacle
                state = "STRAFE_LEFT"
            else:                      # 2nd, 4th ... obstacle
                state = "STRAFE_RIGHT"
            since = t
            print(t, "ms:", state, "- obstacle at", d, "cm")
    elif state == "STRAFE_LEFT" or state == "STRAFE_RIGHT":
        if d >= AVOID_CM and t - since >= STRAFE_MS:
            cleared = cleared + 1
            if cleared >= NUM_OBSTACLES:
                state = "FINISH"
            else:
                state = "FORWARD"
            since = t
            print(t, "ms:", state, "- cleared:", cleared)
    elif state == "FINISH":
        if t - since >= FINISH_MS:
            state = "DONE"
            print(t, "ms:", state, "- motors stopped")
            break
