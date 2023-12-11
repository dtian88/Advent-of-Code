from itertools import combinations

data = open("AoC_2023_11.txt").read().split('\n')
empty_rows = {i for i, line in enumerate(data) if all(c == "." for c in line)}
empty_cols = {j for j in range(len(data[0])) if all(c == "." for c in [line[j] for line in data])}
part1 = part2 = 0

for g1, g2 in combinations({(i, j) for j in range(len(data[0])) for i in range(len(data)) if data[i][j] == "#"}, 2):
  for r in empty_rows:
    if g1[0] < r < g2[0] or g2[0] < r < g1[0]:
      part1 += 1
      part2 += 999999
  for c in empty_cols:
    if g1[1] < c < g2[1] or g2[1] < c < g1[1]:
      part1 += 1
      part2 += 999999
  part1 += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
  part2 += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print('Part 1: %d; part 2: %d' % (part1, part2))
