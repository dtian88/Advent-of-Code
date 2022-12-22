data, moves = open("AoC_2022_22.txt").read().split('\n\n')
next_dir = {
    'L': {
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1)
    },
    'R': {
        (-1, 0): (0, 1),
        (0, -1): (-1, 0),
        (1, 0): (0, -1),
        (0, 1): (1, 0)
    },
}
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
board = []
for i in data.split('\n'):
    board.append(i)
for i in range(len(board)):
    board[i] += ' ' * (len(board[0]) - len(board[i]))
starts_left, starts_right, starts_top, starts_bottom = [], [], [], []
for line in board:
    for i, c in enumerate(line):
        if c != ' ':
            starts_left.append(i)
            break
for line in board:
    for i in range(len(line) - 1, -1, -1):
        if line[i] != ' ':
            starts_right.append(i)
            break
for i in range(len(board[0])):
    for j, line in enumerate(board):
        if line[i] != ' ':
            starts_top.append(j)
            break
for i in range(len(board[0])):
    for j in range(len(board) - 1, -1, -1):
        if board[j][i] != ' ':
            starts_bottom.append(j)
            break
pos, direction, i, current, number_flag = [0, starts_left[0]], (0, 1), 0, '', False
while i <= len(moves):
    if i == len(moves) or not moves[i].isnumeric():
        if number_flag:
            for j in range(int(current)):
                if direction[0] != 0:
                    if starts_top[pos[1]] <= direction[0] + pos[0] <= starts_bottom[pos[1]]:
                        if board[pos[0] + direction[0]][pos[1]] != '#':
                            pos[0] += direction[0]
                        else:
                            break
                    else:
                        if direction[0] == -1:
                            if board[starts_bottom[pos[1]]][pos[1]] != '#':
                                pos[0] = starts_bottom[pos[1]]
                            else:
                                break
                        else:
                            if board[starts_top[pos[1]]][pos[1]] != '#':
                                pos[0] = starts_top[pos[1]]
                            else:
                                break
                else:
                    if starts_left[pos[0]] <= direction[1] + pos[1] <= starts_right[pos[0]]:
                        if board[pos[0]][pos[1] + direction[1]] != '#':
                            pos[1] += direction[1]
                        else:
                            break
                    else:
                        if direction[1] == -1:
                            if board[pos[0]][starts_right[pos[0]]] != '#':
                                pos[1] = starts_right[pos[0]]
                            else:
                                break
                        else:
                            if board[pos[0]][starts_left[pos[0]]] != '#':
                                pos[1] = starts_left[pos[0]]
                            else:
                                break
            number_flag = False
            current = ''
        else:
            if i == len(moves):
                break
            direction = next_dir[moves[i]][direction]
            i += 1
    else:
        current += moves[i]
        number_flag = True
        i += 1
part1 = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dirs.index(direction)

next_moves = dict()
for d in dirs:
    for i, line in enumerate(board):
        for j, c in enumerate(line):
            if c == ' ':
                continue
            if i < 50:
                if 50 <= j < 100:
                    if d[0] == 1:
                        next_moves[(i, j, d)] = (i + 1, j, d)
                    elif d[0] == -1:
                        if i - 1 >= 0:
                            next_moves[(i, j, d)] = (i - 1, j, d)
                        else:
                            next_moves[(i, j, d)] = (150 + j - 50, 0, (0, 1))
                    elif d[1] == 1:
                        next_moves[(i, j, d)] = (i, j + 1, d)
                    else:
                        if j - 1 >= 50:
                            next_moves[(i, j, d)] = (i, j - 1, d)
                        else:
                            next_moves[(i, j, d)] = (100 + (49 - i), 0, (0, 1))
                else:
                    if d[0] == 1:
                        if i + 1 < 50:
                            next_moves[(i, j, d)] = (i + 1, j, d)
                        else:
                            next_moves[(i, j, d)] = (50 + j - 100, 99, (0, -1))
                    elif d[0] == -1:
                        if i - 1 >= 0:
                            next_moves[(i, j, d)] = (i - 1, j, d)
                        else:
                            next_moves[(i, j, d)] = (199, j - 100, d)
                    elif d[1] == 1:
                        if j + 1 < 150:
                            next_moves[(i, j, d)] = (i, j + 1, d)
                        else:
                            next_moves[(i, j, d)] = (100 + (49 - i), 99, (0, -1))
                    else:
                        next_moves[(i, j, d)] = (i, j - 1, d)
            elif 50 <= i < 100:
                if d[1] == 0:
                    next_moves[(i, j, d)] = (i + d[0], j, d)
                elif d[1] == 1:
                    if j + 1 < 100:
                        next_moves[(i, j, d)] = (i, j + 1, d)
                    else:
                        next_moves[(i, j, d)] = (49, 100 + (i - 50), (-1, 0))
                else:
                    if j - 1 >= 50:
                        next_moves[(i, j, d)] = (i, j - 1, d)
                    else:
                        next_moves[(i, j, d)] = (100, i - 50, (1, 0))
            elif 100 <= i < 150:
                if j < 50:
                    if d[0] == 1:
                        next_moves[(i, j, d)] = (i + 1, j, d)
                    elif d[0] == -1:
                        if i - 1 >= 100:
                            next_moves[(i, j, d)] = (i - 1, j, d)
                        else:
                            next_moves[(i, j, d)] = (50 + j, 50, (0, 1))
                    elif d[1] == 1:
                        next_moves[(i, j, d)] = (i, j + 1, d)
                    else:
                        if j - 1 >= 0:
                            next_moves[(i, j, d)] = (i, j - 1, d)
                        else:
                            next_moves[(i, j, d)] = (149 - i, 50, (0, 1))
                else:
                    if d[0] == 1:
                        if i + 1 < 150:
                            next_moves[(i, j, d)] = (i + 1, j, d)
                        else:
                            next_moves[(i, j, d)] = (150 + j - 50, 49, (0, -1))
                    elif d[0] == -1:
                        next_moves[(i, j, d)] = (i - 1, j, d)
                    elif d[1] == 1:
                        if j + 1 < 100:
                            next_moves[(i, j, d)] = (i, j + 1, d)
                        else:
                            next_moves[(i, j, d)] = (149 - i, 149, (0, -1))
                    else:
                        next_moves[(i, j, d)] = (i, j - 1, d)
            else:
                if d[0] == 1:
                    if i + 1 < 200:
                        next_moves[(i, j, d)] = (i + 1, j, d)
                    else:
                        next_moves[(i, j, d)] = (0, j + 100, d)
                elif d[0] == -1:
                    next_moves[(i, j, d)] = (i - 1, j, d)
                elif d[1] == 1:
                    if j + 1 < 50:
                        next_moves[(i, j, d)] = (i, j + 1, d)
                    else:
                        next_moves[(i, j, d)] = (149, 50 + i - 150, (-1, 0))
                else:
                    if j - 1 >= 0:
                        next_moves[(i, j, d)] = (i, j - 1, d)
                    else:
                        next_moves[(i, j, d)] = (0, 50 + i - 150, (1, 0))
pos, direction, i, current, number_flag = [0, starts_left[0]], (0, 1), 0, '', False
while i <= len(moves):
    if i == len(moves) or not moves[i].isnumeric():
        if number_flag:
            for j in range(int(current)):
                next_move_x, next_move_y, next_d = next_moves[(pos[0], pos[1], direction)]
                if board[next_move_x][next_move_y] != '#':
                    pos = (next_move_x, next_move_y)
                    direction = next_d
                else:
                    break
            current = ''
            number_flag = False
        else:
            if i == len(moves):
                break
            direction = next_dir[moves[i]][direction]
            i += 1
    else:
        current += moves[i]
        number_flag = True
        i += 1
print('Part 1: %d; part 2: %d' % (part1, (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dirs.index(direction)))
