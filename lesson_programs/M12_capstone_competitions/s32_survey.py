# Class feedback: how many students are satisfied?
# Answers to "I liked the course": 1 (not at all) ... 5 (very much)
answers = [5, 4, 4, 3, 5, 2, 4, 5, 4, 3, 5, 4]

satisfied = 0
for a in answers:
    if a >= 4:
        satisfied = satisfied + 1

percent = satisfied * 100 / len(answers)
print(f"Satisfied: {satisfied} of {len(answers)} = {percent:.0f} %")
if percent >= 75:
    print("Target of 75 % reached")
else:
    print("Below the target of 75 %")
