import time
from random import randint

print("Rolling the dice ...")
time.sleep(1)                       # wait 1 second (function sleep from module time)
print("You rolled", randint(1, 6))  # a random whole number from 1 to 6
