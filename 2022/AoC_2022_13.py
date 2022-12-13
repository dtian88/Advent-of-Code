from functools import cmp_to_key

data = open("AoC_2022_13.txt").read().strip().split('\n\n')
part1, part2 = 0, 1


def compare(first, second):
    if first and second:
        for idx, token in enumerate(first):
            if idx >= len(second):
                return -1
            if isinstance(token, type(second[idx])):
                result = compare(token, second[idx]) if isinstance(token, list) else second[idx] - token
            else:
                result = compare(token, [second[idx]]) if isinstance(token, list) else compare([token], second[idx])
            if result:
                return result
    return len(second) - len(first)


packets = []
for i, pairs in enumerate(data):
    pair1, pair2 = (eval(pair) for pair in pairs.split('\n'))
    packets.extend([pair1, pair2])
    part1 += i + 1 if compare(pair1, pair2) > 0 else 0
packets.extend([[[2]], [[6]]])
packets.sort(key=cmp_to_key(compare), reverse=True)
for i, c in enumerate(packets):
    if c in ([[2]], [[6]]):
        part2 *= i + 1
print('Part 1: %d; part 2: %d' % (part1, part2))

# def tokens(packet):
#     token_list, idx = [], 0
#     while idx < len(packet):
#         if packet[idx] == "[":
#             temp, lefts, rights = idx + 1, 1, 0
#             while lefts > rights:
#                 if packet[temp] == "[":
#                     lefts += 1
#                 elif packet[temp] == "]":
#                     rights += 1
#                 temp += 1
#             token_list.append(packet[idx:temp])
#             idx = temp + 1
#         else:
#             comma = packet.find(',', idx)
#             token_list.append(packet[idx:comma if comma != -1 else len(packet)])
#             idx = comma + 1 if comma != -1 else len(packet)
#     return token_list
#
#
# def compare(first, second):
#     if first[0] != "[" and second[0] != "[":
#         return int(second) - int(first)
#     first, second = first[1:-1], second[1:-1]
#     tokens_first, tokens_second = tokens(first), tokens(second)
#     if not tokens_first or not tokens_second:
#         return len(tokens_second) - len(tokens_first)
#     for idx, token in enumerate(tokens_first):
#         if idx >= len(tokens_second):
#             return -1
#         if token[0] == '[' and tokens_second[idx][0] == '[' or token[0] != '[' and tokens_second[idx][0] != '[':
#             result = compare(token, tokens_second[idx])
#         else:
#             if token[0] != '[':
#                 result = compare('[' + token + ']', tokens_second[idx])
#             else:
#                 result = compare(token, '[' + tokens_second[idx] + ']')
#         if result:
#             return result
#     return len(first) != len(second)
