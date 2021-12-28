data = open('AoC_2021_4.txt').read().split('\n\n')
part1 = part2 = 0
inputs = list(map(int, data[0].split(',')))
data = [[list(map(int, j.split())) for j in data[i].split('\n')] for i in range(1, len(data))]

inputs_part_2 = inputs.copy()   # for part 2 use
data_part_2 = data.copy()   # for part 2 use

try:
    for i in inputs:
        for board in data:
            for row in board:
                for num in range(len(row)):
                    if row[num] == i:
                        row[num] = -1
            for row in board:
                if sum(row) == -5:
                    s_total = 0
                    for row2 in board:
                        for r in row2:
                            if r != -1:
                                s_total += r
                    part1 = s_total * i
                    raise StopIteration
            for length in range(len(board[0])):
                s = 0
                for row in board:
                    s += row[length]
                if s == -5:
                    s_total = 0
                    for row2 in board:
                        for r in row2:
                            if r != -1:
                                s_total += r
                    part1 = s_total * i
                    raise StopIteration
except StopIteration:
    pass

# part 2
inputs = inputs_part_2
data = data_part_2

try:
    for i in inputs:
        data_2 = []
        for board in data:
            for row in board:
                for num in range(len(row)):
                    if row[num] == i:
                        row[num] = -1
            for row in board:
                if sum(row) == -5:
                    if len(data) == 1:
                        s_total = 0
                        for row2 in board:
                            for r in row2:
                                if r != -1:
                                    s_total += r
                        part2 = s_total * i
                        raise StopIteration
                    data_2.append(board)
                    break
            for length in range(len(board[0])):
                s = 0
                for row in board:
                    s += row[length]
                if s == -5:
                    if len(data) == 1:
                        s_total = 0
                        for row in board:
                            for r in row:
                                if r != -1:
                                    s_total += r
                        part2 = s_total * i
                        raise StopIteration
                    data_2.append(board)
                    break
        for board in data_2:
            if board in data:
                data.remove(board)
except StopIteration:
    pass

print('Part 1: %d; part 2: %d' % (part1, part2))
