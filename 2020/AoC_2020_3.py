data = open("AoC_2020_3.txt").read().split('\n')
count = index = pt1 = 0
for i in range(len(data)):
    data[i] *= 1000
for i in range(0, len(data[0]), 3):
    if data[index][i] == '#':
        count += 1
    index += 1
    if index >= len(data):
        break
pt1 = count

count2 = count3 = count4 = count5 = index = 0
for i in range(0, len(data[0])):
    if data[index][i] == '#':
        count2 += 1
    index += 1
    if index >= len(data):
        break
index = 0
for i in range(0, len(data[0]), 5):
    if data[index][i] == '#':
        count3 += 1
    index += 1
    if index >= len(data):
        break
index = 0
for i in range(0, len(data[0]), 7):
    if data[index][i] == '#':
        count4 += 1
    index += 1
    if index >= len(data):
        break
index = 0
for i in range(0, len(data[0])):
    if data[index][i] == '#':
        count5 += 1
    index += 2
    if index >= len(data):
        break
print('Part 1: %d; part 2: %d' % (pt1, count * count2 * count3 * count4 * count5))