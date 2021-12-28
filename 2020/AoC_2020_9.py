data = list(map(int, open("AoC_2020_9.txt")))
sum_1 = sum_2 = 0
for i in range(25, len(data)):      # part 1
    valid = False
    for j in data[i - 25:i]:
        for k in data[i - 25:i]:
            if j != k and j + k == data[i]:
                valid = True
    if not valid:
        sum_1 = data[i]

sum_nums = set()
for i in range(len(data)):  # part 2
    summed = data[i]
    sum_nums.add(data[i])
    for j in range(i + 1, len(data)):
        summed += data[j]
        sum_nums.add(data[j])
        if summed > 50047984:
            sum_nums.clear()
            break
        elif summed == 50047984:
            sum_2 = min(sum_nums) + max(sum_nums)
print('Part 1: %d; part 2: %d' % (sum_1, sum_2))
