lap_times = [12.5, 11.8, 13.05, 12.1]      # seconds

best = min(lap_times)
average = sum(lap_times) / len(lap_times)

print("Laps:", len(lap_times))
print("Best lap:", best, "s")
print("Average:", round(average, 2), "s")
