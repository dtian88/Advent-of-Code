data = open('AoC_2021_25.txt').read().split('\n')
count = east_col = mask_east = south_row = mask_south = old_east = old_south = 0
east_south = {'>': 0, 'v': 0, '.': 0}
full = 2 ** (len(data) * len(data[0])) - 1
row_shift = (len(data) - 1) * len(data[0])
for i in range(len(data)):
    for j in range(len(data[i])):
        bit_to_add = 2 ** (len(data) * len(data[0]) - 1 - i * len(data[0]) - j)
        east_south[data[i][j]] += bit_to_add
        if j == len(data[i]) - 1:
            east_col += bit_to_add
        if j != 0:
            mask_east += bit_to_add
        if i == len(data) - 1:
            south_row += bit_to_add
        if i != 0:
            mask_south += bit_to_add
mask_west, mask_north, east, south = full ^ east_col, full ^ south_row, east_south['>'], east_south['v']
while old_east ^ east | old_south ^ south:
    old_east, old_south = east, south
    east = east & east_col & (east >> (len(data[0]) - 1) | south >> (len(data[0]) - 1)) |\
        (east & east_col) << (len(data[0]) - 1) & (full ^ (east | south)) |\
        east & mask_west & (east << 1 | south << 1) |\
        (east >> 1 & mask_east & (full ^ (east | south)))
    south = south & south_row & (east >> row_shift | south >> row_shift) |\
        ((south & south_row) << row_shift) & (full ^ (east | south)) |\
        south & mask_north & ((east << len(data[0])) | south << len(data[0])) |\
        (south >> len(data[0]) & mask_south & (full ^ (east | south)))
    count += 1
print(count)


def print_state(e, s):      # just for fun: printing the state from the east and south sea cucumber bitboards
    e_string, s_string = bin(e)[2:], bin(s)[2:]
    e_string = '0' * (len(data) * len(data[0]) - len(e_string)) + e_string
    s_string = '0' * (len(data) * len(data[0]) - len(s_string)) + s_string
    for a in range(len(data) * len(data[0])):
        if a % len(data[0]) == 0:
            print()
        if e_string[a] == '1':
            print('>', end='')
        elif s_string[a] == '1':
            print('v', end='')
        else:
            print('.', end='')


# count = 0     # "dumb way" using strings - my first approach that got the right answer; failed with bitboards at first
# same = False
# while not same:
#     data_old = data.copy()
#     data_temp = data.copy()
#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             if data[i][j] == '>':
#                 compare = 0 if j == len(data[i]) - 1 else j + 1
#                 if data[i][compare] == '.':
#                     data_temp[i] = data_temp[i][:j] + '.' + data_temp[i][j + 1:]
#                     data_temp[i] = data_temp[i][:compare] + '>' + data_temp[i][compare + 1:]
#     data = data_temp.copy()
#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             if data[i][j] == 'v':
#                 compare = 0 if i == len(data) - 1 else i + 1
#                 if data[compare][j] == '.':
#                     data_temp[i] = data_temp[i][:j] + '.' + data_temp[i][j + 1:]
#                     data_temp[compare] = data_temp[compare][:j] + 'v' + data_temp[compare][j + 1:]
#     data = data_temp
#     same = data_old == data
#     count += 1
# print(count)
