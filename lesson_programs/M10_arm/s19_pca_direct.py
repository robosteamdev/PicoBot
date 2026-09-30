from machine import I2C, Pin
from pca9685 import PCA9685
import time

i2c = I2C(1, sda=Pin(2), scl=Pin(3))   # I2C bus 1: GP2 = SDA, GP3 = SCL
pca = PCA9685(i2c)                     # servo driver at address 0x40
pca.freq(50)                           # 50 Hz = one pulse every 20 ms

pca.pwm(2, 0, 307)    # gripper (channel 2): on at step 0, off at step 307
time.sleep(1)         #   307 steps = 1.5 ms = 90 degrees
pca.pwm(2, 0, 375)    # 375 steps = about 1.83 ms = about 120 degrees
time.sleep(1)
pca.pwm(2, 0, 307)    # back to 90 degrees
