data = open("AoC_2022_6.txt").read().strip()

part1 = part2 = -1
for i in range(len(data)):
    if part1 == -1 and len(set(data[i:i + 4])) == 4:
        part1 = i + 4
    if part2 == -1 and len(set(data[i:i + 14])) == 14:
        part2 = i + 14
print('Part 1: %s; part 2: %s' % (part1, part2))
