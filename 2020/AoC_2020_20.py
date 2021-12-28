data = open("AoC_2020_20.txt").read().split('\n\n')
prod = 1        # part 1: didn't actually assemble the puzzle; just checked which four pieces had two unique sides
neighbors = {}
for i in data:
    j = i.split(':\n')[1].replace('\n', '')
    top, bottom, left, right = j[:10], j[-10:], j[::10], j[9::10]
    c = 0
    for k in data:
        if i != k:
            l = k.split(':\n')[1].replace('\n', '')
            orientations = (top, bottom, left, right, top[::-1], bottom[::-1], left[::-1], right[::-1])
            if any(side in orientations for side in (l[:10], l[-10:], l[::10], l[9::10])):
                c += 1
                if j not in neighbors:
                    neighbors[j] = []
                neighbors[j].append(l)
    if c == 2:      # is a corner if there are only two shared sides with another tile
        prod *= int(i.split(':\n')[0].split()[1])

def print_picture(p, s):
    for a in range(s):
        print(p[a * s:a * s + s])

# noinspection PyUnusedLocal
def normal(p, s):       # part 2
    return p

def r90ccw(p, s):
    return ''.join([p[a::s] for a in range(s - 1, -1, -1)])

def flip_r_l(p, s):       # same as r90ccw(flip_h)
    return ''.join([p[a::s] for a in range(s)])

def flip_l_r(p, s):       # same as r90cw(flip_h)
    return ''.join([p[s ** 2 - s + a::-s] for a in range(s - 1, -1, -1)])

def flip_v(p, s):
    return ''.join([p[a:a + s] for a in range(s ** 2 - s, -1, -s)])

def flip_h(p, s):
    return ''.join([p[a:a + s][::-1] for a in range(0, s ** 2, s)])

def r180(p, s):
    return flip_v(flip_h(p, s), s)

def r90cw(p, s):
    return flip_v(flip_l_r(p, s), s)

corners = [i for i, j in neighbors.items() if len(j) == 2]      # a piece is a corner if it has exactly two neighbors
size = 12
picture = [[] for i in range(size)]

commands = [normal, flip_h, flip_v, r180, r90ccw, flip_l_r, flip_r_l, r90cw]
for command in commands:        # orienting the first corner piece correctly
    temp = command(corners[0], 10)
    bottom_count = right_count = 0
    for n in neighbors[corners[0]]:
        for command2 in commands:
            n_2 = command2(n, 10)
            if any(side == temp[-10:] for side in [n_2[:10], n_2[-10:], n_2[::10], n_2[9::10]]):
                bottom_count += 1
            if any(side == temp[9::10] for side in [n_2[:10], n_2[-10:], n_2[::10], n_2[9::10]]):
                right_count += 1
    if bottom_count > 0 and right_count > 0:
        picture[0].append(temp)
        neighbors[temp] = neighbors[corners[0]]
        break

row = 0
while row < size - 1:     # filling out the first column
    bottom = picture[row][0][-10:]
    for i in neighbors[picture[row][0]]:
        for command in commands:
            new_orientation = command(i, 10)
            top = new_orientation[:10]
            if top == bottom:
                row += 1
                picture[row].append(new_orientation)
                neighbors[new_orientation] = neighbors[i]

for row in range(size):       # filling out the rest of the columns
    for col in range(1, size):
        right = picture[row][col - 1][9::10]
        for i in neighbors[picture[row][col - 1]]:
            for command in commands:
                new_orientation = command(i, 10)
                left = new_orientation[::10]
                if left == right:
                    picture[row].append(new_orientation)
                    neighbors[new_orientation] = neighbors[i]

# for i in picture:       # picture is pieced together!
#     for k in range(10):
#         for j in i:
#             print(j[k * 10:k * 10 + 10], end='   ')
#         print()
#     print()

for i in range(size):       # removing the borders
    for j in range(size):
        picture[i][j] = ''.join([picture[i][j][k + 1:k + 9] for k in range(10, 90, 10)])

full = ''       # converting from a grid of pieces to a full picture in one string
for i in picture:
    for k in range(8):
        for j in i:
            full += j[k * 8:k * 8 + 8]
# print_picture(full, 96)

                  #
#    ##    ##    ###    <-- sea monster pattern
 #  #  #  #  #  #

size, sea_monsters = int(pow(len(full), 0.5)), full     # finding sea monsters
for command in commands:
    count, c = 0, command(full, size)
    list_p = [c[i * size:i * size + size] for i in range(size)]
    for i in range(size):
        for j in range(size):
            if list_p[i][j] == '#' and i < size - 2 and 18 <= j < size - 3:     # hard-coded sea monster search
                if list_p[i + 1][j - 18] == '#' and list_p[i + 1][j - 13:j - 11] == '##' and \
                        list_p[i + 1][j - 7:j - 5] == '##' and list_p[i + 1][j - 1:j + 2] == '###' and \
                        list_p[i + 2][j - 17] == '#' and list_p[i + 2][j - 14] == '#' and \
                        list_p[i + 2][j - 11] == '#' and list_p[i + 2][j - 8] == '#' and \
                        list_p[i + 2][j - 5] == '#' and list_p[i + 2][j - 2] == '#':
                    count += 1
                    list_p[i] = list_p[i][:j] + 'O' + list_p[i][j + 1:]      # just for fun, showing
                    temp = list(list_p[i + 1])
                    for r in [18, 13, 12, 7, 6, 1, 0, -1]:
                        temp[j - r] = 'O'
                    list_p[i + 1] = ''.join(temp)                            # where the sea monsters
                    temp = list(list_p[i + 2])
                    for r in [17, 14, 11, 8, 5, 2]:
                        temp[j - r] = 'O'
                    list_p[i + 2] = ''.join(temp)                            # are in the picture
    if count:       # after running the code, there are a total of 15 sea monsters!
        sea_monsters = ''.join(list_p)
        print_picture(sea_monsters, 96)    # print the puzzle with sea monsters highlighted
        print('Part 1: %d; part 2: %d' % (prod, sea_monsters.count('#')))       # or c.count('#') - count * 15
        break