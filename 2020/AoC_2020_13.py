data = open("AoC_2020_13.txt").read().split('\n')
time = int(data[0])     # part 1
least = 100000000
least_bus = -1
nums = data[1].split(',')
for i in nums:
    if i != 'x':
        if int(i) - time % int(i) < least:
            least = int(i) - time % int(i)
            least_bus = int(i)
for i in range(len(nums)):      # part 2
    if data[1].split(',')[i] != 'x':
        if i == 0:
            print(nums[i], i, 0)
        else:
            print(nums[i], i, (int(nums[i]) - i))

# Used Chinese Remainder Theorem calculator online
# Remainders A:     Modulos B:
# 0	                19
# 24	            37
# 580	            599
# 8	                29
# -19	            17
# -19	            23
# 711	            761
# -19	            41
# -50	            13
print('Part 1: %d; part 2: %d' % (least * least_bus, 1012171816131114))