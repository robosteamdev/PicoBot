def travel_time(distance_cm, speed_cm_s=25):
    """Seconds the robot needs for a distance."""
    return distance_cm / speed_cm_s


d = float(input("Distance in cm: "))
t = travel_time(d)
print("At 25 cm/s the robot needs", t, "s")
print("At 40 cm/s it needs", travel_time(d, 40), "s")
