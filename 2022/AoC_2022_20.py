from collections import deque


def decrypt(part=False):
    key = 811589153 if part else 1
    d = nums.copy()
    for _ in range(10 if part else 1):
        for val in original:
            old_idx = d.index(val)
            d.remove(val)
            d.rotate(-val[0] * key % (len(original) - 1))
            d.insert(old_idx, val)
    zero = d.index((0, zero_index))
    return (d[(zero + 1000) % len(d)][0] + d[(zero + 2000) % len(d)][0] + d[(zero + 3000) % len(d)][0]) * key


data = list(map(int, open("AoC_2022_20.txt").read().strip().split('\n')))
idx_to_num, num_to_idx, original, nums, zero_index = dict(), dict(), [], deque(), 0
for i, num in enumerate(data):
    idx_to_num[i] = num, i
    num_to_idx[num, i] = i
    original.append((num, i))
    nums.append((num, i))
    if num == 0:
        zero_index = i
print('Part 1: %d; part 2: %d' % (decrypt(), decrypt(True)))
