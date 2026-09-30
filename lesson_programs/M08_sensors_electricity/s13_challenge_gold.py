# Correction formula: sensor = a * ruler + b (least squares)
ruler = [5, 10, 20, 30, 50, 75, 100]
sensor = [5.5, 10.5, 20.5, 30.6, 50.8, 76.1, 101.1]

n = len(ruler)
mean_x = sum(ruler) / n
mean_y = sum(sensor) / n

top = 0
bottom = 0
for i in range(n):
    top = top + (ruler[i] - mean_x) * (sensor[i] - mean_y)
    bottom = bottom + (ruler[i] - mean_x) ** 2

a = top / bottom
b = mean_y - a * mean_x
print(f"sensor = {a:.4f} * ruler + {b:.2f}")

# use the formula the other way round to correct a reading
reading = 60.9
corrected = (reading - b) / a
print(f"Reading {reading} cm -> corrected {corrected:.1f} cm")
