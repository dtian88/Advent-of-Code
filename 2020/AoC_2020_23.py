data = [6, 5, 3, 4, 2, 7, 9, 1, 8]      # part 1
length = len(data)
current = 0
for i in range(100):
    temp = data[current]
    first, second, third = data[(current + 1) % length], data[(current + 2) % length], data[(current + 3) % length]
    first, second, third = data.pop(data.index(first)), data.pop(data.index(second)), data.pop(data.index(third))
    current = data.index(temp)
    destination = data[current] - 1
    while destination not in data:
        destination -= 1
        if destination < min(data):
            destination = max(data)
    destination = data.index(destination)
    data.insert((destination + 1) % length, first)
    data.insert((destination + 2) % length, second)
    data.insert((destination + 3) % length, third)
    current = (data.index(temp) + 1) % length
pt1 = str(data).replace(', ', '')[2:-1]
data, neighbors = [6, 5, 3, 4, 2, 7, 9, 1, 8], {}      # part 2
for i in range(len(data) - 1):
    neighbors[data[i]] = data[i + 1]
neighbors[data[-1]] = max(data) + 1
for i in range(max(data) + 1, 1000000):
    neighbors[i] = i + 1
neighbors[1000000] = data[0]
current = 6
for i in range(10000000):
    first = neighbors[current]
    second = neighbors[first]
    third = neighbors[second]
    destination = current - 1
    if destination < 1:
        destination = 1000000
    while destination in (first, second, third):
        destination -= 1
        if destination < 1:
            destination = 1000000
    neighbors[current], neighbors[third], neighbors[destination] = neighbors[third], neighbors[destination], first
    current = neighbors[current]
print('Part 1: %s; part 2: %d' % (pt1, neighbors[1] * neighbors[neighbors[1]]))