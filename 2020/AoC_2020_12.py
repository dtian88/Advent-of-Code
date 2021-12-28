data = open("AoC_2020_12.txt").read().split('\n')
dirs = {'N': 1, 'S': -1, 'E': 1, 'W': -1, 'R': 1, 'L': -1, 0: 1, 90: -1, 180: -1, 270: 1}
ns = ew = direction = 0         # part 1
for i in data:
    val = int(i[1:])
    if i[0] in ('N', 'S'):
        ns += val * dirs[i[0]]
    elif i[0] in ('E', 'W'):
        ew += val * dirs[i[0]]
    elif i[0] in ('L', 'R'):
        direction += val * dirs[i[0]]
    else:
        if direction in (0, 180):
            ew += val * dirs[direction]
        else:
            ns += val * dirs[direction]
    direction %= 360
ns_2 = ew_2 = 0         # part 2
w_ns = 1; w_ew = 10
for i in data:
    val = int(i[1:])
    if i[0] in ('N', 'S'):
        w_ns += val * dirs[i[0]]
    elif i[0] in ('E', 'W'):
        w_ew += val * dirs[i[0]]
    elif i[0] in ('L', 'R'):
        if i[0] == 'R':
            val = 360 - val
        if val in (90, 270):
            ns_temp = -w_ew * dirs[val]
            w_ew = w_ns * dirs[val]
        else:
            ns_temp = -w_ns
            w_ew = -w_ew
        w_ns = ns_temp
    else:
        ns_2 += val * w_ns
        ew_2 += val * w_ew
print('Part 1: %d; part 2: %d' % (abs(ns) + abs(ew), abs(ns_2) + abs(ew_2)))
