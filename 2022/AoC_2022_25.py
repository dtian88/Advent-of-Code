data = open("AoC_2022_25.txt").read().split('\n')
snafu, digits = {-1: '-', -2: '=', '-': -1, '=': -2}, []
part1 = sum([(int(c) if c.isnumeric() else snafu[c]) * 5 ** (len(i) - 1 - x) for i in data for x, c in enumerate(i)])
while part1 > 2:
    digits.append(part1 % 5)
    part1 //= 5
digits.append(part1)
for i, d in enumerate(digits):
    if d > 2:
        if i < len(digits) - 1:
            digits[i + 1] += 1
        else:
            digits.append(1)
        digits[i] -= 5
print('Part 1: %s; part 2: %s' % (
    ''.join([str(i) if i >= 0 else snafu[i] for i in reversed(digits)]), 'free! Finished with Advent of Code 2022!!!'))
