from math import prod

games = [l.split(": ")[1].split("; ") for l in open("AoC_2023_2.txt").read().split('\n')]

part1 = part2 = 0
limits = {"red": 12, "green": 13, "blue": 14}
for i, game in enumerate(games):
    possible = True
    cubes = {"red": 0, "green": 0, "blue": 0}
    for subset in game:
        for result in subset.split(", "):
            number, color = result.split(" ")
            if int(number) > limits[color]:
                possible = False
            cubes[color] = max(cubes[color], int(number))
    if possible:
        part1 += i + 1
    part2 += prod(cubes.values())

print('Part 1: %d; part 2: %d' % (part1, part2))
