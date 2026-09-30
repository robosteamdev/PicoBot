# Surface test: points for each surface (example results)
# 2 = works well, 1 = works sometimes, 0 = does not work
surfaces = {
    "white paper": 2,
    "whiteboard": 2,
    "light wooden table": 1,
    "grey cardboard": 0,
}

best = []
for name in surfaces:
    points = surfaces[name]
    print(name, "->", points, "points")
    if points == 2:
        best.append(name)

print("Good surfaces for a track:", best)
