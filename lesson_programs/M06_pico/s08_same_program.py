# This program runs on the computer AND on the Pico.
import sys

voltage = 7.8          # battery voltage in V
cells = 2              # two cells in series
per_cell = voltage / cells

print("Running on:", sys.implementation.name)
print("Voltage per cell:", per_cell, "V")
if per_cell >= 3.5:
    print("Battery OK")
else:
    print("Charge the battery")
