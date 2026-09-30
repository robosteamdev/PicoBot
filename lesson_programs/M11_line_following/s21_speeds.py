# Wheel speeds of the proportional follower
SPEED = 30
TURN = 0.2

print("position, left, right")
for position in [-2, -1, -0.5, 0, 0.5, 1, 2]:
    left = round(SPEED * (1 + TURN * position))
    right = round(SPEED * (1 - TURN * position))
    print(position, left, right)
