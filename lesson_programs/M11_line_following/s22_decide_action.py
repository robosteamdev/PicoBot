# decide_action() from picobot-line_following main.py (v17-2)
def decide_action(sensor_values):
    if all(v == 1 for v in sensor_values):
        return "ON JUNCTION"
    if all(v == 0 for v in sensor_values):
        return "LINE LOST"

    positions = [2, 1, 0, -1, -2]
    weighted_sum = 0
    active_sensors = 0

    for i in range(5):
        if sensor_values[i] == 1:
            weighted_sum += positions[i]
            active_sensors += 1

    if active_sensors > 0:
        weighted_sum = weighted_sum / active_sensors

    if weighted_sum > 1.2:
        return "HARD RIGHT"
    elif weighted_sum > 0.6:
        return "MILD RIGHT"
    elif weighted_sum > 0.2:
        return "SLIGHT RIGHT"
    elif weighted_sum < -1.2:
        return "HARD LEFT"
    elif weighted_sum < -0.6:
        return "MILD LEFT"
    elif weighted_sum < -0.2:
        return "SLIGHT LEFT"
    elif weighted_sum == 0 and any(v == 1 for v in sensor_values):
        return "FORWARD"
    else:
        return "SEARCHING"


for values in [[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0],
               [1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1],
               [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]:
    print(values, decide_action(values))
