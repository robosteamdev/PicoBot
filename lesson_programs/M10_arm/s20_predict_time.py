# Predicted time of a smooth move: number of steps x delay
def move_time(start, target, step=1, delay=0.02):
    steps = abs(target - start) // step + 1
    return steps, steps * delay


for step in [1, 2, 5]:
    steps, seconds = move_time(90, 135, step)
    print(f"90 -> 135, step {step}: {steps} steps, {seconds:.2f} s")
