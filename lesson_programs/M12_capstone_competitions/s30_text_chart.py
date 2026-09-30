# Test results as a bar chart in text - for the poster
results = [("Speed 30", 31.2),
           ("Speed 40", 24.6),
           ("40 + Hard 0.5", 22.8)]

print("Best reliable lap-counting time (s), 3 laps")
for name, seconds in results:
    bar = "#" * round(seconds)      # 1 character = 1 s
    print(f"{name:14} {bar} {seconds}")
