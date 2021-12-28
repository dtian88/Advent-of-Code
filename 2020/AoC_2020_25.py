card_key, door_key = list(map(int, open("AoC_2020_25.txt")))
loop_size, value = 0, 1     # part 1
while value != door_key:
    loop_size, value = loop_size + 1, (value * 7) % 20201227
# while pow(7, loop_size, 20201227) != door_key:    # much slower version that I originally used
#     loop_size += 1
print('Part 1: %s; part 2: %s' % (pow(card_key, loop_size, 20201227), 'free! Finished with Advent of Code 2020!!!'))