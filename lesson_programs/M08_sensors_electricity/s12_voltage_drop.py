# Voltage drop on a shared supply wire (example values)
SUPPLY = 5.0            # V at the regulator
WIRE_R = 0.2            # ohm: wires and connectors together

for current in [0.1, 0.5, 1.0, 2.0]:            # A
    drop = current * WIRE_R                     # V = I * R
    print(f"{current} A -> drop {drop:.2f} V -> "
          f"{SUPPLY - drop:.2f} V at the end of the wire")
