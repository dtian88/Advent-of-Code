data = open("AoC_2022_2.txt").read().split('\n')
pairs = {"A": "X", "B": "Y", "C": "Z"}
win = {"A": "Y", "B": "Z", "C": "X"}
lose = {"A": "Z", "B": "X", "C": "Y"}
scores = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
part1 = 0
for i in data:
    opp, me = i.split()
    if pairs[opp] == me:
        part1 += 3
    elif win[opp] == me:
        part1 += 6
    part1 += scores[me]
part2 = 0
for i in data:
    opp, result = i.split()
    if result == "X":
        part2 += scores[lose[opp]]
    elif result == "Y":
        part2 += scores[pairs[opp]]
    else:
        part2 += scores[win[opp]]
    if result == "Y":
        part2 += 3
    elif result == "Z":
        part2 += 6
print('Part 1: %d; part 2: %d' % (part1, part2))
