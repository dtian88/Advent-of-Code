data = open("AoC_2022_4.txt").read().strip().split('\n')
part1 = part2 = 0
for i in data:
    first, second = i.split(',')
    first_1, first_2 = map(int, first.split('-'))
    second_1, second_2 = map(int, second.split('-'))
    if first_1 <= second_1 and first_2 >= second_2 or second_1 <= first_1 and second_2 >= first_2:
        part1 += 1
    if not(first_1 > second_2 or second_1 > first_2):
        part2 += 1
print('Part 1: %d; part 2: %d' % (part1, part2))
