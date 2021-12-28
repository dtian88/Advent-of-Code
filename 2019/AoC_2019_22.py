data = list(open("AoC_2019_22.txt"))
for i in range(len(data)):
    data[i] = data[i].rstrip()
stack = [i for i in range(10007)]       # first attempt at part 1; working but naive
for i in data:
    if i[:19] == 'deal with increment':
        increment = int(i.split()[-1])
        pointer = 0
        new_stack = [-1 for k in range(10007)]
        for j in range(10007):
            new_stack[pointer] = stack[j]
            pointer = (pointer + increment) % 10007
            while new_stack[pointer] != -1 and j != 10006:
                pointer += 1
                if pointer > 10006:
                    pointer = 0
        stack = new_stack
    elif i == 'deal into new stack':
        stack.reverse()
    else:
        cut_num = int(i.split()[-1])
        stack = stack[cut_num:] + stack[:cut_num]
print(stack.index(2019))


command_list = []       # optimized part 1, failed attempt to figure out part 2
# print(DECK_LENGTH, DECK_LENGTH - SHUFFLE_MULT)
for i in data:
    if i[:19] == 'deal with increment':
        command_list.append((0, int(i.split()[-1])))
    elif i == 'deal into new stack':
        command_list.append((1, 0))
    else:
        command_list.append((2, int(i.split()[-1])))
index = 2019
for i, j in command_list:
    if i == 0:
        index = (index * j) % 10007
    elif i == 1:
        index = (-index - 1) % 10007  # DECK_LENGTH - index - 1
    else:
        index = (index - j) % 10007
print(index)
    # if orig_index == 0:
    # print(orig_index, index, (3224126501264 * orig_index + 46106279852862) % DECK_LENGTH, (pow(index, DECK_LENGTH - 2, DECK_LENGTH) - 46106279852862) / 3224126501264)
# y = (mx + b) % DECK_LENGTH
m = 3224126501264
b = 46106279852862

# x = (inv_mod(y, DECK_LENGTH) - b) / m
# inv_mod(x,n) = pow(x, n - 2, n)
# x = (pow(DECK_LENGTH, y - 2, y) - b) / m

# print(37%5)
# y = pow(5, 37 - 2, 37)
# print(37, 5, y)
# print(5 * y, (5 * y) % 37)


offset = 0; increment = 1       # part 1 with subreddit help
for i in data:
    if i.startswith('deal with increment'):
        increment *= pow(int(i.split()[-1]), 10007 - 2, 10007)
    elif i.startswith('deal into new stack'):
        increment *= -1
        offset += increment
    else:   # 'cut'
        offset += increment * int(i.split()[-1])
print(increment % 10007, offset % 10007, (increment * 2519 + offset) % 10007)   # gets card's value from new position ("reversed")
print((3370 * 2019 + 3249) % 10007)     # manually-obtained increment and offset from looking at outputs; not reversed - gets card's new position from old position


DECK_LENGTH = 119315717514047
SHUFFLE_MULT = 101741582076661
offset = 0; increment = 1       # part 2 with subreddit's help, pretty much ended up copying their code but I sort of understand the math behind it now
for i in data:
    if i.startswith('deal with increment'):
        increment *= pow(int(i.split()[-1]), DECK_LENGTH - 2, DECK_LENGTH)
    elif i.startswith('deal into new stack'):
        increment *= -1
        offset += increment
    else:   # 'cut'
        offset += increment * int(i.split()[-1])
offset *= (1 - pow(increment, SHUFFLE_MULT, DECK_LENGTH)) * pow(1 - increment, DECK_LENGTH - 2, DECK_LENGTH)
increment = pow(increment, SHUFFLE_MULT, DECK_LENGTH)
print((increment * 2020 + offset) % DECK_LENGTH)