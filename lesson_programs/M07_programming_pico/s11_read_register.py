# Ask the motor-board PCA9685 for its PWM frequency
from machine import Pin, I2C
from picobot_motors import MotorDriver

motors = MotorDriver()      # the library sets 50 Hz; no motor moves

i2c = I2C(0, sda=Pin(20), scl=Pin(21))
data = i2c.readfrom_mem(0x40, 0xFE, 1)   # 1 byte from register 0xFE
value = data[0]
freq = 25000000 / (4096 * (value + 1))

print("PRE_SCALE register:", value)
print(f"PWM frequency: {freq:.1f} Hz")
