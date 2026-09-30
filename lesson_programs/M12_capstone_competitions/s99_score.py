# Points of one run in the final mini-challenge
marker = input("Robot reached the marker? (y/n) ")
zone = input("Stopped in the stop zone? (y/n) ")
lifted = input("Cube lifted off the floor? (y/n) ")
ring = int(input("Cube on target: ring 3, 2, 1 or 0? "))
seconds = float(input("Time to the marker in s: "))

points = 0
if marker == "y":
    points = points + 2
    if zone == "y":
        points = points + 1
    if lifted == "y":
        points = points + 2 + ring

print("Points:", points, "of 8")
print("Time:", seconds, "s")
