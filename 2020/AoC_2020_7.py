data = open("AoC_2020_7.txt").read().split('\n')
def r(color):   # part 1
    return 1 if 'shiny gold' in rules[color] else max(r(v) for v in rules[color]) if rules[color] else 0

def r_2(color): # part 2
    return 1 + sum(r_2(v) * num for v, num in rules[color].items()) if rules[color] else 1

rules = dict()
for i in data:
    key = i[:i.index('bag')].strip()
    rules[key] = dict()
    if 'other' not in i:
        for j in [b.strip() for b in [a.strip() for a in i.split('contain')][1].split(', ')]:
            rules[key][j[j.index(' ') + 1:j.index('bag')].strip()] = int(j[:j.index(' ')])
print('Part 1: %d; part 2: %d' % (sum(r(key) for key in rules), r_2('shiny gold') - 1))
