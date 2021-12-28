data = open("AoC_2020_6.txt").read().split('\n\n')
count = count2 = 0
for i in data:
    s = set(i.replace('\n', ''))    # part 1
    count += len(s)
    for j in i.split():             # part 2
        s = s.intersection(j)
    count2 += len(s)
print('Part 1: %d; part 2: %d' % (count, count2))

# one-liners for part 1 and part 2
print(sum(len(set(i)-{'\n'}) for i in data))
print(sum(len(set.intersection(*map(set, i.split('\n')))) for i in data))