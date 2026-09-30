# Practice START/STOP without the competition server.
# Press BOOTSEL = START, press again = STOP.
# Save this file on the Pico as practice_start.py
import rp2
import time


class PracticeStart:
    """Same methods as Competition in the competition library."""

    def __init__(self, run_time_s=60):
        self.running = False
        self.stop_reason = None
        self.mac = "practice"
        self.run_time_ms = run_time_s * 1000
        self.run_id = 0
        self.start_callback = None
        self.stop_callback = None
        self.was_pressed = False
        self.start_time = 0

    def on_start(self, callback):
        self.start_callback = callback

    def on_stop(self, callback):
        self.stop_callback = callback

    def connect(self):
        print("Practice mode: press BOOTSEL to start")

    def stop(self, reason):
        self.running = False
        self.stop_reason = reason
        if self.stop_callback:
            self.stop_callback(self.run_id)

    def poll(self):
        pressed = rp2.bootsel_button() == 1
        new_press = pressed and not self.was_pressed
        self.was_pressed = pressed
        if new_press and not self.running:
            self.running = True
            self.stop_reason = None
            self.start_time = time.ticks_ms()
            self.run_id += 1
            if self.start_callback:
                self.start_callback(self.run_id)
        elif new_press:
            self.stop(None)               # stopped by hand
        elif self.running:
            passed = time.ticks_diff(time.ticks_ms(), self.start_time)
            if passed >= self.run_time_ms:
                self.stop("timeout")      # time limit is over
