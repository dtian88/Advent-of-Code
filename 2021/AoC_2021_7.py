data = list(map(int, open('AoC_2021_7.txt').read().split(',')))
part1 = part2 = float('inf')
for i in data:
    part1 = min(part1, sum([abs(i - j) for j in data]))
    part2 = min(part2, sum([abs(i - j) * (abs(i - j) + 1) // 2 for j in data]))
print('Part 1: %d; part 2: %d' % (part1, part2))
