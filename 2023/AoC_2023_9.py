histories = [[list(map(int, line.split()))] for line in open("AoC_2023_9.txt").read().split('\n')]

for i, history in enumerate(histories):
  while any(histories[i][-1]):
    histories[i].append([b - a for a, b in zip(histories[i][-1][:-1], histories[i][-1][1:])])

for i in range(len(histories)):
  histories[i][-1] = [0, *histories[i][-1], 0]
  for j in range(len(histories[i]) - 2, -1, -1):
    histories[i][j] = [histories[i][j][0] - histories[i][j + 1][0], *histories[i][j], histories[i][j][-1] + histories[i][j + 1][-1]]

print('Part 1: %d; part 2: %d' % (sum(h[0][-1] for h in histories), sum(h[0][0] for h in histories)))
