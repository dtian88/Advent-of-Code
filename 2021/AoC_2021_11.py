def has_greater_9(matrix):
    for a in matrix:
        for b in a:
            if b > 9:
                return True
    return False


data = [list(map(int, list(i))) for i in open('AoC_2021_11.txt').read().split('\n')]
part1 = part2 = step = 0
while True:
    step += 1
    num_flashes = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] += 1
    while has_greater_9(data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] > 9:
                    data[i][j] = 0
                    num_flashes += 1
                    part1 += 1
                    for x in (-1, 0, 1):
                        for y in (-1, 0, 1):
                            if 0 <= i + x < len(data) and 0 <= j + y < len(data[0]) and 0 < data[i + x][j + y] <= 9:
                                data[i + x][j + y] += 1
    if step == 100:
        part1 = step
    if num_flashes == len(data) * len(data[0]):
        part2 = step
        if step >= 100:
            break
print('Part 1: %d; part 2: %d' % (part1, part2))
