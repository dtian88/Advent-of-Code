def yell(m):
    if str(monkeys[m]).isnumeric():
        return 0, 0, monkeys[m]
    m1, op, m2 = monkeys[m].split()
    (_, _, res1), (_, _, res2) = yell(m1), yell(m2)
    return res1, res2, eval(f'{res1} {op} {res2}')


data = open("AoC_2022_21.txt").read().strip().split('\n')
monkeys = dict()
for i in data:
    monkey, val = i.split(': ')
    monkeys[monkey] = int(val) if val.isnumeric() else val
part1 = int(yell('root')[2])
digit, monkeys['humn'] = 0, 9
while True:
    monkey1, monkey2, _ = yell('root')
    if monkey1 <= monkey2:
        break
    digit += 1
    monkeys['humn'] += 9 * 10 ** digit
while True:
    monkey1, monkey2, _ = yell('root')
    if monkey1 == monkey2:
        break
    if monkey1 < monkey2:
        monkeys['humn'] -= 10 ** digit
        monkey1, monkey2, _ = yell('root')
        if monkey1 > monkey2:
            monkeys['humn'] += 10 ** digit
            digit -= 1
print('Part 1: %d; part 2: %d' % (part1, monkeys['humn']))
