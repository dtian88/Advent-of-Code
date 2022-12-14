def simulate(part, g):  # @param part: False = part 1; True = part 2
    res, g = 0, [[c if c != 'o' else '.' for c in line] for line in g]
    while True:
        loc = [0, 500]
        while True:
            if not part and loc[0] == max_y:
                return res
            if g[loc[0] + 1][loc[1]] == '.':
                loc[0] += 1
            elif loc[1] - 1 >= 0 and g[loc[0] + 1][loc[1] - 1] == '.':
                loc = [loc[0] + 1, loc[1] - 1]
            elif loc[1] + 1 < len(g[0]) and g[loc[0] + 1][loc[1] + 1] == '.':
                loc = [loc[0] + 1, loc[1] + 1]
            elif loc[1] + 1 == len(g[0]) and loc[0] < max_y + 1:
                for line in range(max_y + 3):
                    g[line].extend(['.'] if line != max_y + 2 else ['#'])
                loc = [loc[0] + 1, loc[1] + 1]
            else:
                res += 1
                g[loc[0]][loc[1]] = 'o'
                if part and loc == [0, 500]:
                    return res
                break


data = open("AoC_2022_14.txt").read().strip().split('\n')
max_x = max_y = 0
for i in data:
    points = i.split(' -> ')
    for point in points:
        x, y = point.split(',')
        max_x, max_y = max(max_x, int(x)), max(max_y, int(y))
grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for i in data:
    points = i.split(' -> ')
    for j in range(len(points) - 1):
        first_x, first_y = tuple(map(int, points[j].split(',')))
        second_x, second_y = tuple(map(int, points[j + 1].split(',')))
        if first_x == second_x:
            for k in range(min(first_y, second_y), max(first_y, second_y) + 1):
                grid[k][first_x] = "#"
        else:
            for k in range(min(first_x, second_x), max(first_x, second_x) + 1):
                grid[first_y][k] = "#"
grid.extend([['.' for _ in range(max_x + 1)], ['#' for _ in range(max_x + 1)]])
print('Part 1: %d; part 2: %d' % (simulate(False, grid), simulate(True, grid)))
