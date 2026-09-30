lap_times = [13, 12, 14, 12]       # seconds


def average(values):
    total = 0
    for t in values:               # go through the list
        total = total + t
    return total / len(values)     # len() replaces count


print("Average:", average(lap_times))
