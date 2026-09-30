voltage = 7.2              # battery voltage in V
cells = 2

per_cell = voltage / cells
print("Per cell:", per_cell)
if voltage < 7.0:
    print("Charge the battery!")
else:
    print("Battery OK")
