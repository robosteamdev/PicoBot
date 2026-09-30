# Speed of sound in air at different temperatures
ECHO = 5831                  # the same echo time in µs

for temp in [0, 10, 20, 30]:
    speed = 331.3 + 0.606 * temp          # m/s
    distance = ECHO * speed / 10000 / 2   # m/s -> cm per µs: / 10000
    print(f"{temp:3} °C: {speed:.1f} m/s -> {distance:.1f} cm")

print("The program always uses 343 m/s ->", round(ECHO * 0.0343 / 2, 1), "cm")
