data = open('AoC_2021_20.txt').read().split('\n')
algorithm = data[0]
data = ['..' + i + '..' for i in data[2:]]
data.extend(['.' * len(data[0]), '.' * len(data[0])])
data.insert(0, '.' * len(data[0]))
data.insert(0, '.' * len(data[0]))
mod_list = ['.', '#']

count = 0
for z in range(1, 51):
    data2 = data.copy()
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            s = ''
            for a in (-1, 0, 1):
                for b in (-1, 0, 1):
                    s += data[i + a][j + b]
            data2[i] = data2[i][:j] + algorithm[int(s.replace('.', '0').replace('#', '1'), 2)] + data2[i][j + 1:]
    data = data2
    for i in range(len(data)):
        a = list(data[i])
        for j in range(len(a)):
            if i < 1 or j < 1 or i >= len(data) - 1 or j >= len(data[0]) - 1:
                a[j] = mod_list[z % 2]
        data[i] = ''.join(a)
    data = [mod_list[z % 2] + i + mod_list[z % 2] for i in data]
    data.append(mod_list[z % 2] * len(data[0]))
    data.insert(0, mod_list[z % 2] * len(data[0]))
    if z == 2:
        count = sum([i.count('#') for i in data])

print('Part 1: %d; part 2: %d' % (count, sum([i.count('#') for i in data])))
