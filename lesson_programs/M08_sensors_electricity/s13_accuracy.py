# Accuracy of the ultrasonic sensor (example results of one team)
# ruler distance in cm : five sensor readings in cm
data = {
    5: [5.6, 5.4, 5.5, 5.7, 5.3],
    10: [10.4, 10.6, 10.5, 10.3, 10.7],
    20: [20.3, 20.6, 20.4, 20.5, 20.7],
    30: [30.6, 30.4, 30.8, 30.5, 30.7],
    50: [50.9, 50.6, 51.0, 50.7, 50.8],
    75: [75.9, 76.3, 75.8, 76.1, 76.4],
    100: [101.2, 100.8, 101.5, 101.0, 101.0],
}

print("ruler  average  error  error %  spread")
for ruler in data:
    readings = data[ruler]
    average = sum(readings) / len(readings)
    error = average - ruler
    percent = error / ruler * 100
    spread = max(readings) - min(readings)
    print(f"{ruler:5} {average:8.1f} {error:6.1f} {percent:8.1f} {spread:7.1f}")
