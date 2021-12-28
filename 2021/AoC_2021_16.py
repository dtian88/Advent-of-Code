data = open('AoC_2021_16.txt').read().split('\n')[0]
part1 = 0
binary = bin(int(data, 16))[2:]
binary = '0' * (len(data) * 4 - len(binary)) + binary


def recur(b, limit):
    global part1
    packet_version = int(b[0:3], 2)
    packet_type = int(b[3:6], 2)
    part1 += packet_version
    if packet_type != 4:
        length_type = b[6]
        if length_type == '0':          # operator packet specifying max sub-packet length
            num_packets = 1
            max_length = int(b[7:22], 2)
            sub_packet_values = recur(b[22:22 + max_length], False)[2]  # don't care about number of sub-sub-packets;
            return_list = operation(packet_type, sub_packet_values)     # a packet with a sub-packet that also contains
            if not limit and '1' in b[22 + max_length:]:                # a sub-packet is only counted as having one
                a, c, d = recur(b[22 + max_length:], False)             # sub-packet.
                num_packets += a
                max_length += c
                return_list.extend(d)
            return num_packets, 22 + max_length, return_list
        else:                           # operator packet specifying max # of sub-packets
            max_packets = int(b[7:18], 2)
            num_packets = 1
            length = 18
            sub_packet_values = []
            while max_packets > 0:
                temp, temp2, temp3 = recur(b[length:], True)
                max_packets -= temp
                length += temp2
                sub_packet_values.extend(temp3)
            return_list = operation(packet_type, sub_packet_values)
            if not limit and '1' in b[length:]:
                a, c, d = recur(b[length:], False)
                num_packets += a
                length += c
                return_list.extend(d)
            return num_packets, length, return_list
    else:                               # packet representing a literal value
        number = ''
        index = 6
        while index < len(b):
            number += b[index + 1:index + 5]
            if b[index] == '0':
                break
            index += 5
        index += 5
        return_list = [int(number, 2)]
        if not limit and '1' in b[index:]:  # or limit > 0):
            a, c, d = recur(b[index:], False)
            return_list.extend(d)
            return 1 + a, index + c, return_list
        else:
            return 1, index, return_list


def operation(packet, ret_list):
    if packet == 0:
        return [sum(ret_list)]
    if packet == 1:
        product = 1
        for i in ret_list:
            product *= i
        return [product]
    if packet == 2:
        return [min(ret_list)]
    if packet == 3:
        return [max(ret_list)]
    if packet == 5:
        return [ret_list[0] > ret_list[1]]
    if packet == 6:
        return [ret_list[0] < ret_list[1]]
    return [ret_list[0] == ret_list[1]]


part2 = recur(binary, -1)[2][0]
print('Part 1: %d; part 2: %d' % (part1, part2))
