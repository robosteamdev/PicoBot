# START and STOP - simulated on the computer
class FakeCompetition:
    """Works like the competition library, but the messages
    come from a list: one message for each poll()."""

    def __init__(self, messages):
        self.messages = messages
        self.running = False
        self.stop_reason = None
        self.run_id = 0
        self.start_callback = None
        self.stop_callback = None

    def on_start(self, callback):
        self.start_callback = callback

    def on_stop(self, callback):
        self.stop_callback = callback

    def poll(self):
        if not self.messages:
            return
        msg = self.messages.pop(0)
        if msg == "START":
            self.running = True
            self.stop_reason = None
            self.run_id += 1
            self.start_callback(self.run_id)   # like the library
        elif msg in ("finished", "timeout"):
            self.running = False
            self.stop_reason = msg
            self.stop_callback(self.run_id)


def when_start(run_id):
    print("START received for run", run_id, "- motors on")


def when_stop(run_id):
    print("STOP received - motors off, reason:", comp.stop_reason)


# "" = no message during this poll
comp = FakeCompetition(["", "", "START", "", "", "", "finished"])
comp.on_start(when_start)       # give the library our functions
comp.on_stop(when_stop)

for loop in range(1, 8):
    comp.poll()                 # check for a message
    if comp.running:
        print("loop", loop, "- driving")
    else:
        print("loop", loop, "- waiting")
