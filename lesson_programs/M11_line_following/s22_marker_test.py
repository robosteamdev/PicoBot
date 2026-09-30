# Is it the marker? Test on the computer


def is_marker(values):
    """True when all five sensors see black."""
    return values == [1, 1, 1, 1, 1]


tests = [[0, 0, 1, 0, 0],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0],
         [0, 1, 1, 1, 0]]

for t in tests:
    if is_marker(t):
        print(t, "-> marker")
    else:
        print(t, "-> no marker")
