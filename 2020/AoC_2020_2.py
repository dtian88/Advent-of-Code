data = open("AoC_2020_2.txt").read().split('\n')
count = count_part_2 = 0
for i in data:
    letter = i.split()[1][0]
    minimum, maximum = map(int, i.split()[0].split('-'))
    s = i.split()[-1]
    count2 = sum(j == letter for j in s)
    if minimum <= count2 <= maximum:
        count += 1
    if s[minimum - 1] == letter and s[maximum - 1] != letter or s[minimum - 1] != letter and s[maximum - 1] == letter:
        count_part_2 += 1
print('Part 1: %d; part 2: %d'%(count, count_part_2))