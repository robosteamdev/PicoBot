# Mecanum mixing: wanted movement -> four wheel values.
# forward: + forward, - backward
# right:   + sideways right, - sideways left
# turn:    + clockwise (right), - counter-clockwise


def mix(forward, right, turn):
    fl = forward + right + turn
    fr = forward - right - turn
    bl = forward - right + turn
    br = forward + right - turn
    return fl, fr, bl, br           # four values at once


def show(name, forward, right, turn):
    fl, fr, bl, br = mix(forward, right, turn)
    print(f"{name:16} FL {fl:4} FR {fr:4} BL {bl:4} BR {br:4}")


show("forward", 50, 0, 0)
show("sideways right", 0, 50, 0)
show("turn right", 0, 0, 50)
show("forward-right", 25, 25, 0)
show("rear axle right", 0, 25, 25)
