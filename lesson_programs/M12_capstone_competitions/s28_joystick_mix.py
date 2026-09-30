# From joystick position to four wheel speeds (as in session 16)
MAX_SPEED = 60      # speed at full joystick deflection
DEAD_ZONE = 0.1     # small deflections count as 0


def shape(value):
    """Joystick value -1.0 ... 1.0 -> speed, with a dead zone."""
    if abs(value) < DEAD_ZONE:
        return 0
    return round(value * MAX_SPEED)


def mix(forward, right, turn):
    fl = forward + right + turn
    fr = forward - right - turn
    bl = forward - right + turn
    br = forward + right - turn
    return [max(-100, min(100, v)) for v in (fl, fr, bl, br)]


# (joystick x = right, joystick y = forward, rotation)
tests = [(0.0, 1.0, 0.0), (1.0, 0.0, 0.0), (0.7, 0.7, 0.0),
         (0.05, 0.5, 0.0), (1.0, 1.0, 0.5)]
for x, y, r in tests:
    wheels = mix(shape(y), shape(x), shape(r))
    print(f"x={x:5} y={y:5} r={r:4} -> FL FR BL BR = {wheels}")
