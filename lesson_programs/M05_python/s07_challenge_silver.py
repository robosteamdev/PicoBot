times = []
for i in range(5):
    t = float(input("Lap time " + str(i + 1) + " in s: "))
    times.append(t)

print("Best:", min(times), "s")
print("Worst:", max(times), "s")
print("Average:", round(sum(times) / len(times), 2), "s")
