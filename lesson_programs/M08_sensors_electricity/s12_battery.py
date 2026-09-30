# The PicoBot battery pack: 2 cells in series
CELLS = 2
CAPACITY_AH = 3.0                  # 3000 mAh (example cell)

for name, cell_v in [("full", 4.2), ("nominal", 3.7),
                     ("recharge", 3.5), ("empty", 3.0)]:
    print(f"{name:9} {cell_v} V per cell -> pack {CELLS * cell_v:.1f} V")

energy = CELLS * 3.7 * CAPACITY_AH             # E = V * Ah, in Wh
print(f"Stored energy: about {energy:.1f} Wh")
