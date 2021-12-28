import math


def reduce(result):
    while True:
        explode_index = split_index = -1
        for j in range(len(result)):
            if result[j] == ',' and result.count('[', 0, j) - result.count(']', 0, j) >= 5:
                explode_index = j
                break
        if explode_index != -1:  # explode
            first_number = int(result[result.rfind('[', 0, explode_index) + 1:explode_index])
            second_number = int(result[explode_index + 1:result.find(']', explode_index)])
            first_digit_index = last_digit_index = -1
            for k in range(result.rfind('[', 0, explode_index), -1, -1):
                if result[k].isdigit():
                    first_digit_index = k
                    break
            if first_digit_index != -1:
                while result[first_digit_index].isdigit():
                    first_digit_index -= 1
                first_digit_index += 1
                end_first_digit_index = first_digit_index
                while result[end_first_digit_index].isdigit():
                    end_first_digit_index += 1
                first_digit_replace = int(result[first_digit_index:end_first_digit_index]) + first_number
                result = result[0:first_digit_index] + str(first_digit_replace) + result[end_first_digit_index:]
                explode_index += len(str(first_digit_replace)) - len(result[first_digit_index:end_first_digit_index])

            for k in range(explode_index + len(str(second_number)) + 1, len(result)):
                if result[k].isdigit():
                    last_digit_index = k
                    break
            if last_digit_index != -1:
                end_last_digit_index = last_digit_index
                while result[end_last_digit_index].isdigit():
                    end_last_digit_index += 1
                last_digit_replace = int(result[last_digit_index:end_last_digit_index]) + second_number
                result = result[0:last_digit_index] + str(last_digit_replace) + result[end_last_digit_index:]
            result = result[:result.rfind('[', 0, explode_index)] + '0' + result[result.find(']', explode_index) + 1:]
        else:
            for j in range(len(result)):
                if result[j].isdigit():
                    min_index = j
                    while result[min_index].isdigit():
                        min_index += 1
                    num = int(result[j:min_index])
                    if num > 9:
                        split_index = j
                        break
            if split_index != -1:  # split
                end_index = split_index
                while result[end_index].isdigit():
                    end_index += 1
                num = int(result[split_index:end_index])
                result = result[0:split_index] + '[' + str(num // 2) + ',' + str(math.ceil(num / 2)) + ']' + result[
                                                                                                             end_index:]
            else:
                break
    return result


def magnitude(result):
    while ',' in result:
        for p in range(len(result)):
            if result[p] == ',' and result[p - 1].isdigit() and result[p + 1].isdigit():
                start_bracket = result.rfind('[', 0, p)
                end_bracket = result.find(']', p)
                result = result[0:start_bracket] + str(
                    3 * int(result[start_bracket + 1:p]) + 2 * int(result[p + 1:end_bracket])) + result[
                                                                                                 end_bracket + 1:]
                break
    return int(result)


data = open('AoC_2021_18.txt').read().split('\n')
r = data[0]  # part 1
for i in range(1, len(data)):
    r = reduce('[' + r + ',' + data[i] + ']')

max_magnitude = 0  # part 2
for a in range(len(data)):
    for b in range(a + 1, len(data)):
        mag_1 = magnitude(reduce('[' + data[a] + ',' + data[b] + ']'))
        mag_2 = magnitude(reduce('[' + data[b] + ',' + data[a] + ']'))
        max_magnitude = max(mag_1, mag_2) if max(mag_1, mag_2) > max_magnitude else max_magnitude

print('Part 1: %d; part 2: %d' % (magnitude(r), max_magnitude))
