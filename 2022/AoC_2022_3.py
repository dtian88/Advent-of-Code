data = open("AoC_2022_3.txt").read().split('\n')
part1 = 0
mapping = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in data:
    first, second = i[:len(i) // 2], i[len(i) // 2:]
    c = set(first).intersection(set(second)).pop()
    # if ord(c) >= 97:
    #     part1 += ord(c) - 96
    # else:
    #     part1 += ord(c) - 38
    part1 += mapping.index(c)
part2 = 0
for i in range(0, len(data), 3):
    c = set(data[i]).intersection(set(data[i + 1]).intersection(set(data[i + 2]))).pop()
    # if ord(c) >= 97:
    #     part2 += ord(c) - 96
    # else:
    #     part2 += ord(c) - 38
    part2 += mapping.index(c)
print('Part 1: %d; part 2: %d' % (part1, part2))
