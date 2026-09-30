# Calibration of one PicoBot at speed 50 (example values).
drive_time = 2.0                    # seconds
runs_cm = [41.5, 43.0, 42.0]        # three runs, forward

average_cm = sum(runs_cm) / len(runs_cm)
speed = average_cm / drive_time     # cm per second
time_10cm = 10 / speed

print(f"Average distance: {average_cm:.1f} cm")
print(f"Speed: {speed:.1f} cm/s")
print(f"Time for 10 cm: {time_10cm:.2f} s")

# Turn: 0.5 s gave these angles (degrees)
test_time = 0.5
angles = [62, 58, 60]
average_angle = sum(angles) / len(angles)
time_90 = test_time * 90 / average_angle
print(f"Estimated time for 90 degrees: {time_90:.2f} s")
