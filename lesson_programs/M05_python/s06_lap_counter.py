laps = int(input("How many laps? "))

for crossing in range(1, laps + 2):
    if crossing == 1:
        print("Crossing 1: start of lap 1")
    elif crossing <= laps:
        print(f"Crossing {crossing}: lap {crossing - 1} done, start of lap {crossing}")
    else:
        print(f"Crossing {crossing}: lap {laps} done - STOP on the marker")
