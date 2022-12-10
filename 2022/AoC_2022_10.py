data = open("AoC_2022_10.txt").read().strip().split('\n')
part1, register, cycle = 0, 1, 1
pixels, crt = [["." for _ in range(40)] for _ in range(6)], [0, 0]
for i in data:
    for j in range(1 if i == "noop" else 2):
        if cycle in range(20, 221, 40):
            part1 += cycle * register
        if j == 1 and i != "noop":
            register += int(i.split()[1])
        if crt[1] in (register - 2, register - 1, register):
            pixels[crt[0]][crt[1]] = "#"
        crt = [crt[0] + (crt[1] + 1) // 40, (crt[1] + 1) % 40]
        cycle += 1
for line in pixels:
    for pixel in line:
        print(pixel, end="")
    print()
print('Part 1: %s; part 2: %s' % (part1, "REHPRLUB"))
