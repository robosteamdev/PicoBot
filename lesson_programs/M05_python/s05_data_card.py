robot = input("Robot name: ")
team = input("Team name: ")
voltage = float(input("Battery voltage in V: "))

per_cell = voltage / 2      # two cells in series

print("===== PicoBot data card =====")
print("Robot:  ", robot)
print("Team:   ", team)
print("Battery:", voltage, "V")
print("Cells:  ", per_cell, "V per cell")
print("=============================")
