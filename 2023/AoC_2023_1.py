data = open("AoC_2023_1.txt").read().split('\n')

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
           "nine": "9"}

part1 = part2 = 0
for line in data:
    str_1, str_2 = "", ""
    for i in range(len(line)):
        if line[i].isnumeric():
            str_1 += line[i]
            str_2 += line[i]
        else:
            for number in numbers:
                if line[i:].startswith(number):
                    str_2 += numbers[number]
    if str_1:
        part1 += int(str_1[0] + str_1[-1])
    if str_2:
        part2 += int(str_2[0] + str_2[-1])

print('Part 1: %d; part 2: %d' % (part1, part2))
