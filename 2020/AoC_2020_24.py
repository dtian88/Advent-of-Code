data = open("AoC_2020_24.txt").read().split('\n')
black = set()       # part 1
for i in data:
    coordinate = [0, 0]
    flag = ''
    for j in range(len(i)):
        if i[j] == 'e' and not flag:
            coordinate[0] += 1
        elif i[j] == 'w' and not flag:
            coordinate[0] -= 1
        elif i[j] == 's' or i[j] == 'n':
            flag = i[j]
            continue
        else:
            if flag + i[j] == 'nw':
                if not coordinate[1] % 2:
                    coordinate[0] -= 1
                coordinate[1] -= 1
            elif flag + i[j] == 'ne':
                if coordinate[1] % 2:
                    coordinate[0] += 1
                coordinate[1] -= 1
            elif flag + i[j] == 'sw':
                if not coordinate[1] % 2:
                    coordinate[0] -= 1
                coordinate[1] += 1
            else:
                if coordinate[1] % 2:
                    coordinate[0] += 1
                coordinate[1] += 1
            flag = ''
    if tuple(coordinate) in black:
        black.remove(tuple(coordinate))
    else:
        black.add(tuple(coordinate))
pt1 = len(black)

def get_neighbors(c1, c2):      # part 2
    neighbor_set = {(c1 - 1, c2), (c1 + 1, c2)}
    if c2 % 2:
        neighbor_set = neighbor_set.union({(c1, c2 - 1), (c1 + 1, c2 - 1), (c1 + 1, c2 + 1), (c1, c2 + 1)})
    else:
        neighbor_set = neighbor_set.union({(c1 - 1, c2 - 1), (c1, c2 - 1), (c1, c2 + 1), (c1 - 1, c2 + 1)})
    return neighbor_set

white = set()
for i in range(100):
    for b in black:
        white = white.union(get_neighbors(b[0], b[1]).difference(black))
    temp_black, temp_white = black.copy(), white.copy()
    for b in black:
        n = get_neighbors(b[0], b[1])
        if n.isdisjoint(black) or len(n.intersection(black)) > 2:
            temp_black.remove(b)
            temp_white.add(b)
    for w in white:
        n = get_neighbors(w[0], w[1])
        if len(n.intersection(black)) == 2:
            temp_black.add(w)
            temp_white.remove(w)
    black, white = temp_black, temp_white
print('Part 1: %s; part 2: %d' % (pt1, len(black)))
