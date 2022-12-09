data = open("AoC_2022_8.txt").read().strip().split('\n')
part2 = 0
seen = set()
for i in range(len(data)):
    for j in range(len(data[i])):
        n = s = e = w = 0
        i2 = i - 1
        while i2 >= 0:
            n += 1
            if int(data[i2][j]) >= int(data[i][j]):
                break
            i2 -= 1
        i2 = i + 1
        while i2 < len(data):
            s += 1
            if int(data[i2][j]) >= int(data[i][j]):
                break
            i2 += 1
        j2 = j - 1
        while j2 >= 0:
            e += 1
            if int(data[i][j2]) >= int(data[i][j]):
                break
            j2 -= 1
        j2 = j + 1
        while j2 < len(data[0]):
            w += 1
            if int(data[i][j2]) >= int(data[i][j]):
                break
            j2 += 1
        part2 = max(part2, n * s * e * w)

        if i == 0 or j == 0 or i == len(data) - 1 or j == len(data[0]) - 1:
            seen.add((i, j))
        else:
            s = True
            for i2 in range(i):
                if int(data[i2][j]) >= int(data[i][j]):
                    s = False
                    break
            if s:
                seen.add((i, j))
                continue
            s = True
            for i2 in range(i + 1, len(data)):
                if int(data[i2][j]) >= int(data[i][j]):
                    s = False
                    break
            if s:
                seen.add((i, j))
                continue
            s = True
            for j2 in range(j + 1, len(data[0])):
                if int(data[i][j2]) >= int(data[i][j]):
                    s = False
                    break
            if s:
                seen.add((i, j))
                continue
            s = True
            for j2 in range(j):
                if int(data[i][j2]) >= int(data[i][j]):
                    s = False
                    break
            if s:
                seen.add((i, j))
                continue
print('Part 1: %s; part 2: %s' % (len(seen), part2))
