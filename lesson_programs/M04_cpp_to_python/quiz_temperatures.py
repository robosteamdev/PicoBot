temps = [21, 23, 22, 25, 26]      # degrees C


def average(values):
    total = 0
    for t in values:
        total += t
    return total / len(values)    # / already gives decimals


avg = average(temps)
print("Average:", avg)
if avg > 23.0:
    print("Warm")
else:
    print("OK")
