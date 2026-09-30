# How long do you hold the BOOTSEL button?
import rp2
import time

print("Hold the BOOTSEL button ...")
while rp2.bootsel_button() == 0:    # wait until it is pressed
    pass                            # pass = do nothing
start = time.ticks_ms()
while rp2.bootsel_button() == 1:    # wait until it is released
    pass
duration = time.ticks_diff(time.ticks_ms(), start)
print("You held it for", duration, "ms")
