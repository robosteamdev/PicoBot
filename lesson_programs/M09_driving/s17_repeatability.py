# Repeatability of a timed 90-degree turn (example values).
angles = [88, 93, 90, 85, 91]       # five runs, same time

average = sum(angles) / len(angles)
spread = max(angles) - min(angles)

print("Runs:", len(angles))
print(f"Average: {average:.1f} degrees")
print(f"Spread: {spread} degrees ({min(angles)} to {max(angles)})")
