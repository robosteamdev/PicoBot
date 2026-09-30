import random

secret = random.randint(1, 100)     # a random whole number from 1 to 100
tries = 0

while True:
    guess = int(input("Your guess (1-100): "))
    tries = tries + 1
    if guess < secret:
        print("Too small")
    elif guess > secret:
        print("Too big")
    else:
        print("Correct! You needed", tries, "tries.")
        break
    if tries == 7:
        print("No more tries. The number was", secret)
        break
