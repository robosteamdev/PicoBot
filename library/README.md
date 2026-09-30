# PicoBot library

Copy these files into the **main folder** of the Pico (in Thonny: View → Files, select the files, right-click →
**Upload to /**). The lesson programs import them.

| File | What it does |
|---|---|
| `picobot_motors.py` | the four wheel motors (motor driver board, I2C on GP20/GP21) |
| `picobot_arm.py` | the three servos of the arm (servo driver board, I2C on GP2/GP3), with safe angle limits |
| `pca9685.py` | driver of the PCA9685 boards (used by the two files above) |
| `picobot.py` | the `PicoBot` class: forward, backward, sideways, diagonal and turning moves, and the arm |

Check a new robot first with the test programs of <https://github.com/robosteamdev/picobot-setup>.
