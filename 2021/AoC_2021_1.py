data = list(map(int, open("AoC_2021_1.txt").read().split('\n')))
count = 0
for x in range(1, len(data)):
    if data[x] > data[x - 1]:
        count += 1

count2 = 0
for x in range(1, len(data) - 2):
    if data[x] + data[x + 1] + data[x + 2] > data[x - 1] + data[x] + data[x + 1]:
        count2 += 1

print('Part 1: %d; part 2: %d' % (count, count2))
# print('Part 1: %d; part 2: %d' % (sum([data[i] > data[i - 1] for i in range(1, len(data))]), sum(
#     data[i] + data[i + 1] + data[i + 2] > data[i - 1] + data[i] + data[i + 1] for i in range(1, len(data) - 2))))
