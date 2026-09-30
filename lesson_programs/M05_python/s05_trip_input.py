# Ask for the speed and the time, then calculate the distance.

speed = int(input("Speed in cm per second: "))
time = int(input("Driving time in seconds: "))

distance = speed * time
print("The robot drives", distance, "cm")
