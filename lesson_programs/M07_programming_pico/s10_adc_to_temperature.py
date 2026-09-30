# From ADC number to temperature (runs on the computer too)


def to_voltage(raw):
    return raw * 3.3 / 65535


def to_celsius(raw):
    voltage = to_voltage(raw)
    return 27 - (voltage - 0.706) / 0.001721


for raw in [13600, 14000, 14200, 14400]:
    print(f"raw {raw}: {to_voltage(raw):.4f} V -> {to_celsius(raw):.1f} °C")
