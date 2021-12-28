data = open('AoC_2021_9.txt').read().split('\n')
for i in range(len(data)):
    data[i] = '?' + data[i] + '?'
data.insert(0, '?' * len(data[0]))
data.append('?' * len(data[0]))
count = 0
low = set()
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        value = int(data[i][j])
        if (data[i - 1][j] == '?' or int(data[i - 1][j]) > value) and (
                data[i + 1][j] == '?' or int(data[i + 1][j]) > value) and (
                data[i][j - 1] == '?' or int(data[i][j - 1]) > value) and (
                data[i][j + 1] == '?' or int(data[i][j + 1]) > value):
            count += value + 1
            low.add((i, j))

max1 = max2 = max3 = -1  # part 2
basins = []
for i, j in low:
    size = 0
    visited = set()
    queue = [(i, j)]
    while queue:
        x, y = queue.pop(0)
        if (x, y) not in visited:
            size += 1
            visited.add((x, y))
            for a in (-1, 0, 1):
                for b in (-1, 0, 1):
                    if (a != 0 or b != 0) and a * b == 0 and data[x + a][y + b] not in ('?', '9') and (
                            x + a, y + b) not in visited:
                        queue.append((x + a, y + b))
    basins.append(size)
basins.sort(reverse=True)
print('Part 1: %d; part 2: %d' % (count, basins[0] * basins[1] * basins[2]))
