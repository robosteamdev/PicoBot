left = 1        # 1 = this sensor sees the black line
right = 0

if left == 1 and right == 1:
    print("Both sensors on the line: drive straight")
elif left == 1 or right == 1:
    print("Only one sensor on the line: turn a little")
else:
    print("Line lost: search!")
