# Weighted line position - try it on the computer

WEIGHTS = [2, 1, 0, -1, -2]      # D1 ... D5 (right -> left)


def line_position(values):
    """Average weight of the sensors that see the line.
    None = no sensor sees the line."""
    total = 0
    count = 0
    for i in range(5):
        if values[i] == 1:
            total = total + WEIGHTS[i]
            count = count + 1
    if count == 0:
        return None
    return total / count


tests = [[0, 0, 1, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]

for t in tests:
    print(t, "->", line_position(t))
