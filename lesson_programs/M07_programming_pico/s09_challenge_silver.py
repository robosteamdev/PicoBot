import rp2
import time


def wait_for_press():
    while rp2.bootsel_button() == 1:    # first wait until released
        pass
    while rp2.bootsel_button() == 0:    # then wait for a new press
        pass
    time.sleep_ms(20)                   # ignore bouncing


print("Press BOOTSEL to start ...")
wait_for_press()
start = time.ticks_ms()
print("Running - press again to stop")
wait_for_press()
seconds = time.ticks_diff(time.ticks_ms(), start) / 1000
print(f"Time: {seconds:.2f} s")
