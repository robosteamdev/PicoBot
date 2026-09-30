# How long does Python need to count to one million?
import time

start = time.time()            # time in seconds
count = 0
while count < 1000000:
    count += 1
end = time.time()

print("Counted to", count)
print("Time:", round(end - start, 3), "s")
