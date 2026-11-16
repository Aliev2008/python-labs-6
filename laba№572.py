n = int(input())
stats = {}

for _ in range(n):
    team1, goals1, team2, goals2 = input().split(';')
    goals1, goals2 = int(goals1), int(goals2)

    for team in (team1, team2):
        if team not in stats:
            stats[team] = [0, 0, 0, 0, 0]  # games, wins, draws, losses, points
        stats[team][0] += 1

    if goals1 > goals2:
        stats[team1][1] += 1
        stats[team1][4] += 3
        stats[team2][3] += 1
    elif goals1 < goals2:
        stats[team2][1] += 1
        stats[team2][4] += 3
        stats[team1][3] += 1
    else:
        stats[team1][2] += 1
        stats[team2][2] += 1
        stats[team1][4] += 1
        stats[team2][4] += 1

for team, s in stats.items():
    print(f"{team}:", *s)
