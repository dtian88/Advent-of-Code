import re
data = open("AoC_2020_4.txt").read().split('\n\n')
count = 0  # part 1
for i in data:
    if i.count(':') == 8 or (i.count(':') == 7 and i.find('cid') == -1):
        count += 1
count2 = 0  # part 2
for passport in data:
    if not (passport.count(':') == 8 or (passport.count(':') == 7 and passport.find('cid') == -1)):
        continue
    valid = True
    for field in passport.split():
        val = field.split(':')[1]
        if field.startswith('byr') and not 1920 <= int(val) <= 2002 or \
                field.startswith('iyr') and not 2010 <= int(val) <= 2020 or \
                field.startswith('eyr') and not 2020 <= int(val) <= 2030 or \
                field.startswith('ecl') and val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or \
                field.startswith('pid') and not (len(val) == 9 and val.isnumeric()) or \
                field.startswith('hgt') and not (field.endswith('cm') or field.endswith('in')) or \
                field.find('in') != -1 and not 59 <= int(val[:val.index('in')]) <= 76 or \
                field.find('cm') != -1 and not 150 <= int(val[:val.index('cm')]) <= 193 or \
                field.startswith('hcl') and not re.search(r'#[0-9a-f]{6}', val):
            valid = False
    count2 += 1 if valid else 0
print('Part 1: %d; part 2: %d' % (count, count2))

        # elif field.startswith('hcl'):     # non-regex search
            # for k in val[1:]:
            #     if k not in '0123456789abcdef':
            #         valid = False
