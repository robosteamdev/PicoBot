# Speed or reliability? Analyse the test log on the computer.
# Each setting: the base speed and the times of 3 runs in s.
# None = the run failed (the robot lost the line).
log = {
    30: [31.2, 30.8, 31.5],
    40: [24.9, 25.3, 24.6],
    50: [20.1, None, 20.8],
    60: [None, 17.9, None],
}


def summary(times):
    """Number of finished runs, best time, spread of the times."""
    ok = []
    for t in times:
        if t is not None:
            ok.append(t)
    if len(ok) == 0:
        return 0, None, None
    return len(ok), min(ok), max(ok) - min(ok)


safe_speed = None
print("Speed  Finished  Best (s)  Spread (s)")
for speed in log:
    n, best, spread = summary(log[speed])
    if n == 0:
        print(f"{speed:5}  0 of 3    -         -")
        continue
    print(f"{speed:5}  {n} of 3    {best:.1f}      {spread:.1f}")
    if n == 3:
        safe_speed = speed      # the fastest so far with 3 of 3

print("Fastest setting with 3 of 3 finished runs:", safe_speed)
