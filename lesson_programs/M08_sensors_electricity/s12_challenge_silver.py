# Check the two cells of a PicoBot battery pack
MAX_DIFFERENCE = 0.1            # our rule for this exercise, in V

cell1 = float(input("Voltage of cell 1 in V: "))
cell2 = float(input("Voltage of cell 2 in V: "))

pack = cell1 + cell2            # in series the voltages add up
print(f"Pack voltage: {pack:.2f} V")

if pack < 7.0:
    print("Charge now")
else:
    print("OK for driving")

if abs(cell1 - cell2) > MAX_DIFFERENCE:
    print("Tell your teacher: the cells are different")
