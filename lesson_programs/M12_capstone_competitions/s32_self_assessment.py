# My self-assessment: which modules need more practice?
# 3 = I can do it alone, 2 = with help, 1 = not yet
ratings = {
    "M05 Python": 3,
    "M07 Pico inputs and outputs": 2,
    "M09 Driving": 3,
    "M10 Arm": 2,
    "M11 Line following": 3,
    "M12 Competitions": 1,
}

total = 0
for module in ratings:
    total = total + ratings[module]
print(f"Average: {total / len(ratings):.1f} of 3")

print("Next goals:")
for module in ratings:
    if ratings[module] < 3:
        print("-", module)
