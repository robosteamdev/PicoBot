# Height test: which heights worked? (example results of one team)
# Each row: height above normal in mm, white test OK?, line test OK?
results = [
    [0, True, True],
    [3, True, True],
    [6, True, True],
    [9, True, False],
    [12, False, False],
]

working = []
for row in results:
    height = row[0]
    if row[1] and row[2]:
        working.append(height)
        print("+", height, "mm: OK")
    else:
        print("+", height, "mm: FAILED")

print("The calibration works up to", max(working), "mm higher.")
