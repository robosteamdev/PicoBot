robot = {"name": "Speedy", "team": "Blue Sharks", "speed": 50}

print(robot["name"])            # Speedy
robot["speed"] = 70             # change a value
robot["laps"] = 3               # add a new pair

for key in robot:
    print(key, "=", robot[key])
