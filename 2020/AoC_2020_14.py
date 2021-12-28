data = open("AoC_2020_14.txt").read().split('\n')
memory = dict()         # part 1
mask = 0
for i in data:
    if i.startswith('mask'):
        mask = i.split(' = ')[1]
    else:
        val = int(i.split(' = ')[1])
        num = 0
        for j in range(len(mask)):
            if mask[j] != 'X':
                num |= int(mask[j]) << (len(mask) - j - 1)
            elif j > len(mask) - len(bin(val)) - 2:
                num |= val & (1 << (len(mask) - j - 1))
        memory[int(i[i.index('[') + 1:i.index(']')])] = num

def recur(m, value):        # part 2
    if m in visited:
        return
    visited.add(m)
    if 'X' not in m:
        memory2[int(m, 2)] = value
        return
    for bit in range(len(m)):
        if m[bit] == 'X':
            recur(m[:bit] + '0' + m[bit + 1:], value)
            recur(m[:bit] + '1' + m[bit + 1:], value)

memory2 = dict()
for i in data:
    if i.startswith('mask'):
        mask = i.split(' = ')[1]
    else:
        index = bin(int(i[i.index('[') + 1:i.index(']')]))[2:]
        result = ''
        while len(index) < len(mask):
            index = '0' + index
        for j in range(len(index)):
            if mask[j] == 'X':
                result += 'X'
            elif mask[j] == '1':
                result += '1'
            else:
                result += index[j]
        visited = set()
        recur(result, int(i.split(' = ')[1]))
print('Part 1: %d; part 2: %d' % (sum(memory.values()), sum(memory2.values())))