data = list(map(int, open("AoC_2020_10.txt")))
data.extend([0, max(data) + 3])  # part 1, calculation in print method
data.sort()
count, i = 1, 0  # part 2
while i < len(data) - 1:
    j, c = 0, 1
    while data[i + j + 1] - data[i + j] < 3:
        c += j + 1 - (data[i + j + 1] - data[i + j])
        j += 1
    count *= c
    i += j + 1
print('Part 1: %d; part 2: %d' % (sum(data[i] - data[i - 1] == 1 for i in range(len(data))) * sum(
    data[i] - data[i - 1] == 3 for i in range(len(data))), count))