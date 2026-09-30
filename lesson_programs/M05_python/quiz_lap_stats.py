def average(values):
    return sum(values) / len(values)


laps = int(input("How many laps? "))
times = []
for lap in range(1, laps + 1):
    t = float(input(f"Time of lap {lap} in s: "))
    times.append(t)

avg = average(times)
print(f"Best lap: {min(times):.2f} s")
print(f"Average: {avg:.2f} s")

if avg < 12:
    print("Fast team!")
else:
    print("Keep training!")
