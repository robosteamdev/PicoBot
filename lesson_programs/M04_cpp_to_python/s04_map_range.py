# Arduino's map() written in Python.
# It scales x from the range in_min..in_max to out_min..out_max.

def map_range(x, in_min, in_max, out_min, out_max):
    # the same whole-number maths as Arduino's map()
    scaled = (x - in_min) * (out_max - out_min)
    return scaled // (in_max - in_min) + out_min


# Arduino: analogRead() gives 0 ... 1023
print("Arduino:", map_range(512, 0, 1023, 0, 255))
# Pico: read_u16() gives 0 ... 65535 -> scale to 0 ... 100 %
print("Pico:", map_range(32768, 0, 65535, 0, 100), "%")
