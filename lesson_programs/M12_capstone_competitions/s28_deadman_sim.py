# Deadman idea: the robot drives only while messages keep coming
TIMEOUT_MS = 300     # no message for 300 ms -> stop

# times (ms) when the phone sent "drive forward"
messages = [0, 100, 200, 300, 400, 900, 1000]

last_msg = None
moving = False
for now in range(0, 1500, 100):     # the robot checks every 100 ms
    if now in messages:
        last_msg = now
        if not moving:
            print(now, "ms: message - motors ON")
        moving = True
    elif moving and now - last_msg > TIMEOUT_MS:
        moving = False
        print(now, "ms: no message for", now - last_msg,
              "ms - motors OFF")
