count = count2 = 0
data = open("AoC_2020_11.txt").read().split('\n')  # part 1
rows = len(data); cols = len(data[0])
while True:
    prev = data.copy()
    for i in range(rows):
        for j in range(cols):
            if prev[i][j] != '.':
                c = sum(d_i | d_j and 0 <= i + d_i < rows and 0 <= j + d_j < cols and prev[i + d_i][j + d_j] == '#'
                    for d_j in [-1, 0, 1] for d_i in [-1, 0, 1])
                if c == 0 and prev[i][j] == 'L':
                    data[i] = data[i][:j] + '#' + data[i][j + 1:]
                elif c >= 4 and prev[i][j] == '#':
                    data[i] = data[i][:j] + 'L' + data[i][j + 1:]
    if data == prev:
        count = ''.join(data).count('#')
        break
data = open("AoC_2020_11.txt").read().split('\n')  # part 2
while True:
    prev = data.copy()
    for i in range(rows):
        for j in range(cols):
            if prev[i][j] != '.':
                c = 0
                for d_i in [-1, 0, 1]:
                    for d_j in [-1, 0, 1]:
                        if d_i | d_j:
                            temp_i = i + d_i; temp_j = j + d_j
                            while 0 <= temp_i < rows and 0 <= temp_j < cols:
                                if prev[temp_i][temp_j] in ['#', 'L']:
                                    if prev[temp_i][temp_j] == '#':
                                        c += 1
                                    break
                                temp_i += d_i; temp_j += d_j
                if c == 0 and prev[i][j] == 'L':
                    data[i] = data[i][:j] + '#' + data[i][j + 1:]
                elif c >= 5 and prev[i][j] == '#':
                    data[i] = data[i][:j] + 'L' + data[i][j + 1:]
    if data == prev:
        count2 = ''.join(data).count('#')
        break
print('Part 1: %d; part 2: %d' % (count, count2))