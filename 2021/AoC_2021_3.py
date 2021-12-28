data = open("AoC_2021_3.txt").read().split('\n')
a = len(data[0])
most = least = ""
for i in range(a):
    count0 = count1 = 0
    for j in data:
        if int(j[i]) == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        most += "0"
        least += "1"
    else:
        most += "1"
        least += "0"

# part 2
most_2 = least_2 = ""
for i in range(a):
    data_2 = []
    bit = ""
    count0 = count1 = 0
    for j in data:
        if int(j[i]) == 0:
            count0 += 1
        else:
            count1 += 1
    bit = "0" if count0 > count1 else "1"
    for j in data:
        if j[i] == bit:
            data_2.append(j)
    data = data_2
    if len(data) == 1:
        most_2 = data[0]
        break


data = open("AoC_2021_3.txt").read().split('\n')
for i in range(a):
    data_2 = []
    bit = ""
    count0 = count1 = 0
    for j in data:
        if int(j[i]) == 0:
            count0 += 1
        else:
            count1 += 1
    bit = "1" if count0 > count1 else "0"
    for j in data:
        if j[i] == bit:
            data_2.append(j)
    data = data_2
    if len(data) == 1:
        least_2 = data[0]
        break

print('Part 1: %d; part 2: %d' % (int(most, 2) * int(least, 2), int(most_2, 2) * int(least_2, 2)))
