# Ohm's law and power: current through a resistor
VOLTAGE = 3.3                      # V (the Pico's logic voltage)

for resistance in [330, 1000, 10000]:           # ohm
    current = VOLTAGE / resistance              # I = V / R, in A
    power = VOLTAGE * current                   # P = V * I, in W
    print(f"{resistance:6} ohm: {current * 1000:5.2f} mA, "
          f"{power * 1000:6.2f} mW")
