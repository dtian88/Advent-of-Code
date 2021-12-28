# data = list(map(int, open('AoC_2021_6.txt').read().split(',')))   # old part 1
# for i in range(80):
#     j = len(data)
#     for d in range(j):
#         if data[d] != 0:
#             data[d] -= 1
#         else:
#             data[d] = 6
#             data.append(8)
# print(len(data))
data = list(map(int, open('AoC_2021_6.txt').read().split(',')))
frequencies = dict()
for i in range(9):
    frequencies[i] = sum([i == j for j in data])
part1 = 0
for i in range(256):
    num_zeros = frequencies[0]
    for j in range(1, 9):
        frequencies[j - 1] = frequencies[j]
    frequencies[6] += num_zeros
    frequencies[8] = num_zeros
    if i == 79:
        part1 = sum(frequencies.values())
print('Part 1: %d; part 2: %d' % (part1, sum(frequencies.values())))
