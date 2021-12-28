data = open("AoC_2020_5.txt").read().split('\n')
seat_list = []
highest = 0  # part 1
for i in data:
    lower, upper, col_lower, col_upper = 0, 127, 0, 7
    for j in i:
        if j == 'F':
            upper = (lower + upper) // 2
        elif j == 'B':
            lower = (lower + upper) // 2 + 1
        elif j == 'L':
            col_upper = (col_lower + col_upper) // 2
        else:
            col_lower = (col_lower + col_upper) // 2 + 1
    highest = max(highest, lower * 8 + col_lower)
    seat_list.append(lower * 8 + col_lower)

# One-liner for part 1 (inputs are simply binary numbers)
print(max(int(i.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for i in
          open("AoC_2020_5.txt").read().split('\n')))

seat_list = sorted(seat_list)  # part 2
for i in range(len(seat_list) - 1):
    if seat_list[i + 1] - seat_list[i] == 2:
        print('Part 1: %d; part 2: %d' % (highest, seat_list[i] + 1))
