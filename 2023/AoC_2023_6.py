data = open("AoC_2023_6.txt").read().split('\n\n')
part1, part2 = 1, 0

pairs = [(44, 208), (80, 1581), (65, 1050), (72, 1102), (44806572, 208158110501102)]
for idx, pair in enumerate(pairs):
  temp = 0
  for speed in range(1, pair[0]):
    if speed * (pair[0] - speed) > pair[1]:
      if idx == len(pairs) - 1:
        part2 += 1
      else:
        temp += 1
  part1 *= max(1, temp)
print('Part 1: %d; part 2: %d' % (part1, part2))
