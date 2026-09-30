# The mission as a state machine - simulated on the computer
# Each step of ARM_SEQ: (what the robot does, wait time in ms)
ARM_SEQ = [("base 45 deg to the first side", 600),
           ("close the gripper", 600),
           ("arm to the carry angle", 600),
           ("base 45 deg to the other side", 600),
           ("lower the arm", 600),
           ("open the gripper", 600),
           ("arm to the carry angle", 600),
           ("drive back about 10 cm", 600),
           ("turn 180 deg", 1000)]

state = "IDLE"
step = 0          # number of the current ARM_SEQ step
step_start = 0    # time (ms) when this step started


def change(new_state, now):
    """Go to a new state and print the transition."""
    global state, step, step_start
    print(now, "ms:", state, "->", new_state)
    state = new_state
    step = 0
    step_start = now


def update(now, start, marker):
    """One run of the state machine - on the robot a timer
    calls it every 50 ms."""
    global step, step_start
    if state == "IDLE":
        if start:
            change("OUTBOUND", now)
    elif state == "OUTBOUND":
        if marker:
            change("ARM_SEQ", now)
            print(now, "ms:   ", ARM_SEQ[0][0])
    elif state == "ARM_SEQ":
        wait = ARM_SEQ[step][1]
        if now - step_start >= wait:      # this step is done
            step = step + 1
            step_start = now
            if step < len(ARM_SEQ):
                print(now, "ms:   ", ARM_SEQ[step][0])
            else:
                change("RETURNING", now)
    elif state == "RETURNING":
        if marker:
            change("DONE", now)


# A recorded test run: START at 0 ms, the end marker at
# 4000 ms, the start marker at 14000 ms.
for now in range(0, 16000, 50):
    start = (now == 0)
    marker = now in (4000, 14000)
    update(now, start, marker)
