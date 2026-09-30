# Results of a timed category: best run, ranking, points
PENALTY_S = 5        # example school rule: 5 s per penalty
POINTS = [10, 8, 6, 4, 2, 1]   # position points 1st ... 6th

# Each team: list of runs (time in s, penalties).
# None = the run did not finish.
runs = {
    "Sharks": [(26.4, 0), (24.9, 1), None],
    "Owls":   [(23.8, 2), (25.1, 0), (24.7, 0)],
    "Robins": [None, (31.0, 0), (29.5, 0)],
    "Foxes":  [None, None, None],
}


def run_time(run):
    """Time of one run including the penalty seconds."""
    seconds, penalties = run
    return seconds + penalties * PENALTY_S


best = []            # pairs (best time, team)
for team in runs:
    times = []
    for run in runs[team]:
        if run is not None:
            times.append(run_time(run))
    if times:
        best.append((min(times), team))
    else:
        print(team, "- no finished run")

best.sort()          # the shortest time first
for place in range(len(best)):
    seconds, team = best[place]
    points = POINTS[place] if place < len(POINTS) else 0
    print(f"{place + 1}. {team:7} {seconds:5.1f} s  {points} points")
