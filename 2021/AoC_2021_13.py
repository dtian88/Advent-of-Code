data = open('AoC_2021_13.txt').read().split('\n')
count = -1
instructions = [tuple(i.split('=')) for i in data[data.index('') + 1:]]
points = set(tuple(map(int, i.split(','))) for i in data[:data.index('')])
for direction, i in instructions:
    instruction = int(i)
    toRemove = set()
    toAdd = set()
    if direction[-1] == 'x':
        for point in points:
            if point[0] > instruction:
                toAdd.add((instruction - (point[0] - instruction), point[1]))
                toRemove.add(point)
    else:
        for point in points:
            if point[1] > instruction:
                toAdd.add((point[0], instruction - (point[1] - instruction)))
                toRemove.add(point)
    points = points.difference(toRemove)
    points = points.union(toAdd)
    if count == -1:
        count = len(points)
grid = [['.' for i in range(max(points)[0] + 1)] for j in range(max(points)[1] + 1)]
for (x, y) in points:
    grid[y][x] = '#'
for line in grid:
    for letter in line:
        print(letter, end=' ')
    print()
print('\nPart 1: %d; part 2: %s' % (count, 'CPZLPFZL'))
