SPEED = 40
TURN = 0.25
pos = 2
left = round(SPEED * (1 + TURN * pos))
right = round(SPEED * (1 - TURN * pos))
print(left, right)
