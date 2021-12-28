data = open("AoC_2020_19.txt").read().split('\n\n')
rule_list, rules = data[0].split('\n'), {}      # part 1
for i in rule_list:
    num, rule = i.split(': ')
    rules[num] = rule
def recur(n):
    if n == '53':
        return 'a'
    if n == '90':
        return 'b'
    possibles = []
    for order in rules[n].split(' | '):
        if ' ' in order:
            possibles.extend(combos(recur(order.split()[0]), recur(order.split()[1])))
        else:
            possibles.extend(recur(order))
    return possibles

def combos(t1, t2):
    return [c1 + c2 for c2 in t2 for c1 in t1]

zero = set(recur('0'))

forty_two, thirty_one = set(recur('42')), set(recur('31'))      # part 2
count = 0
for message in data[1].split('\n'):
    index = count_42 = count_31 = 0
    while message[index:index + 8] in forty_two:
        count_42 += 1
        index += 8
    while message[index:index + 8] in thirty_one:
        count_31 += 1
        index += 8
    if count_31 and count_42 > count_31 and index == len(message):
        count += 1
print('Part 1: %d; part 2: %d' % (sum(message in zero for message in data[1].split('\n')), count))