data = open("AoC_2022_9.txt").read().strip().split('\n')
visited_1, visited_2 = {(0, 0)}, {(0, 0)}
rope_1, rope_2 = [[0, 0] for _ in range(2)], [[0, 0] for _ in range(10)]
moves = {"L": (0, -1), "R": (0, 1), "D": (1, -1), "U": (1, 1)}
for i in data:
    move, length = i.split()[0], int(i.split()[1])
    for _ in range(length):
        for rope in (rope_1, rope_2):
            rope[0][moves[move][0]] += moves[move][1]
        for rope in (rope_1, rope_2):
            for k in range(1, len(rope)):
                if (abs(rope[k - 1][0] - rope[k][0]) + abs(rope[k - 1][1] - rope[k][1]) == 2 and abs(
                        rope[k - 1][0] - rope[k][0]) != abs(rope[k - 1][1] - rope[k][1])) or (
                        abs(rope[k - 1][0] - rope[k][0]) + abs(rope[k - 1][1] - rope[k][1]) > 2):
                    rope[k][0] += int((rope[k - 1][0] - rope[k][0]) / abs(rope[k - 1][0] - rope[k][0])) if abs(
                        rope[k - 1][0] - rope[k][0]) else 0
                    rope[k][1] += int((rope[k - 1][1] - rope[k][1]) / abs(rope[k - 1][1] - rope[k][1])) if abs(
                        rope[k - 1][1] - rope[k][1]) else 0
        visited_1.add(tuple(rope_1[-1]))
        visited_2.add(tuple(rope_2[-1]))
print('Part 1: %s; part 2: %s' % (len(visited_1), len(visited_2)))
