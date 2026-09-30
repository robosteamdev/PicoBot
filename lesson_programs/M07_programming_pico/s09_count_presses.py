# Count how many times the BOOTSEL button is pressed
import rp2
import time

count = 0
previous = 0                # the button in the last loop: 0 = up

while True:
    now = rp2.bootsel_button()
    if now == 1 and previous == 0:      # it was up, now it is down
        count = count + 1
        print("Presses:", count)
    previous = now                      # remember for the next loop
    time.sleep_ms(20)
