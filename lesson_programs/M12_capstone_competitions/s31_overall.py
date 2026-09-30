# Overall ranking: add the position points of all categories
line_following = ["Owls", "Sharks", "Robins"]    # 1st, 2nd, 3rd
object_manip = ["Sharks", "Robins", "Owls", "Foxes"]
POINTS = [10, 8, 6, 4, 2, 1]

total = {}
for ranking in [line_following, object_manip]:
    for place in range(len(ranking)):
        team = ranking[place]
        points = POINTS[place] if place < len(POINTS) else 0
        total[team] = total.get(team, 0) + points

order = sorted(total, key=lambda t: total[t], reverse=True)
for team in order:
    print(team, total[team])
