import helpers

route = [50, 120, 30]           # three straight parts of a route, in cm

total = 0
for part in route:
    total = total + helpers.travel_time(part)

print("Total driving time:", total, "s")
print("Average part:", round(helpers.average(route), 1), "cm")
