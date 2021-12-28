data = open('AoC_2021_5.txt').read().split('\n')
data = [[list(map(int, j.split(','))) for j in i.split(' -> ')] for i in data]
count1 = count2 = 0
points = set()
seen = set()
for i in data:
    if i[0][0] == i[1][0]:
        for j in range(min(i[0][1], i[1][1]), max(i[0][1], i[1][1]) + 1):
            p = (i[0][0], j)
            if p in points:
                if p not in seen:
                    count1 += 1
                    seen.add(p)
            else:
                points.add(p)
    elif i[0][1] == i[1][1]:
        for j in range(min(i[0][0], i[1][0]), max(i[0][0], i[1][0]) + 1):
            p = (j, i[0][1])
            if p in points:
                if p not in seen:
                    count1 += 1
                    seen.add(p)
            else:
                points.add(p)

points.clear()
seen.clear()
for i in data:
    if i[0][0] > i[1][0]:
        temp = i[0]
        i[0] = i[1]
        i[1] = temp
    if i[0][0] != i[1][0]:
        for j in range(0, i[1][0] - i[0][0] + 1):
            p = (j + i[0][0], j * (i[1][1] - i[0][1]) / (i[1][0] - i[0][0]) + i[0][1])
            if p in points:
                if p not in seen:
                    count2 += 1
                    seen.add(p)
            else:
                points.add(p)
    else:
        for j in range(min(i[0][1], i[1][1]), max(i[0][1], i[1][1]) + 1):
            p = (i[0][0], j)
            if p in points:
                if p not in seen:
                    count2 += 1
                    seen.add(p)
            else:
                points.add(p)
print('Part 1: %d; part 2: %d' % (count1, count2))

