total = int(input("Time in seconds: "))
minutes = total // 60       # whole minutes
seconds = total % 60        # what is left
print(total, "s =", minutes, "min", seconds, "s")
