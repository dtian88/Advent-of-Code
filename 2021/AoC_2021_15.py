from collections import defaultdict
from queue import PriorityQueue

data = open('AoC_2021_15.txt').read().split('\n')
data2 = [['0' for i in range(5 * len(data[0]))] for j in range(5 * len(data))]

for i in range(len(data)):  # part 2 setup
    for j in range(len(data[i])):
        temp = temp2 = data[i][j]
        data2[i][j] = temp
        for k in range(1, 5):
            temp = '1' if temp == '9' else str(int(temp) + 1)
            temp2 = '1' if temp2 == '9' else str(int(temp2) + 1)
            data2[i + len(data) * k][j] = temp
            data2[i][j + len(data) * k] = temp2

for i in range(len(data), len(data) * 5):
    for j in range(len(data[0])):
        temp = data2[i][j]
        for k in range(1, 5):
            temp = '1' if temp == '9' else str(int(temp) + 1)
            data2[i][j + len(data) * k] = temp

data2 = [''.join(i) for i in data2]


def djikstra(d):
    for i in range(len(d)):
        d[i] = '?' + d[i] + '?'
    d.insert(0, '?' * len(d[0]))
    d.append('?' * len(d[0]))
    neighbors = defaultdict(set)
    for i in range(1, len(d) - 1):
        for j in range(1, len(d[i]) - 1):
            if d[i + 1][j] != '?':
                neighbors[(i, j)].add((i + 1, j))
            if d[i - 1][j] != '?':
                neighbors[(i, j)].add((i - 1, j))
            if d[i][j + 1] != '?':
                neighbors[(i, j)].add((i, j + 1))
            if d[i][j - 1] != '?':
                neighbors[(i, j)].add((i, j - 1))
    pq = PriorityQueue()
    visited = set()
    dists = {i: float('inf') for i in neighbors}
    dists[(1, 1)] = 0
    pq.put((0, (1, 1)))
    while not pq.empty():
        dist, v = pq.get()
        if v not in visited:
            visited.add(v)
            for neighbor in neighbors[v]:
                if neighbor not in visited and dists[v] + int(d[neighbor[0]][neighbor[1]]) < dists[neighbor]:
                    dists[neighbor] = dists[v] + int(d[neighbor[0]][neighbor[1]])
                pq.put((dists[neighbor], neighbor))
    return dists[(len(d) - 2, len(d) - 2)]


print('Part 1: %d; part 2: %d' % (djikstra(data), djikstra(data2)))
