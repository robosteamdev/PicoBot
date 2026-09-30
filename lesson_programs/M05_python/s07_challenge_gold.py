def square_plan(side_cm):
    plan = []
    for side in range(4):
        plan.append("forward " + str(side_cm) + " cm")
        plan.append("turn right 90°")
    return plan


for step in square_plan(50):
    print(step)
