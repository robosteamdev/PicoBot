# From echo time to distance (HC-SR04)
SPEED = 0.0343        # speed of sound: 343 m/s = 0.0343 cm per µs

echo_times = [583, 1166, 2915, 5831]     # echo pulse in µs

for t in echo_times:
    distance = t * SPEED / 2             # there and back: divide by 2
    print(t, "µs ->", round(distance, 1), "cm")
