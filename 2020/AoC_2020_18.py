from collections import deque
data = open("AoC_2020_18.txt").read().split('\n')
total = 0       # part 1
for i in data:
    i = i.replace(' ', '')
    stack = deque()
    for j in range(len(i)):
        if i[j] == '(':
            stack.append(j)
    while stack:
        incr, index = 1, stack.pop()
        prev_answer = i[index + incr]
        while prev_answer.isnumeric():
            incr += 1
            prev_answer += i[index + incr]
        incr -= 1
        prev_answer = int(prev_answer[:-1])
        while True:
            incr += 1
            operation = i[index + incr]
            if operation == ')':
                i = i[:index] + str(prev_answer) + i[i.find(')', index) + 1:]
                break
            incr += 1
            num = i[index + incr]
            while num.isnumeric():
                incr += 1
                num += i[index + incr]
            num = int(num[:-1])
            incr -= 1
            if operation == '+':
                prev_answer += num
            else:
                prev_answer *= num
    incr, index, prev_answer = 1, -1, i[0]
    while prev_answer.isnumeric():
        incr += 1
        prev_answer += i[index + incr]
    incr -= 1
    prev_answer = int(prev_answer[:-1])
    while True:
        incr += 1
        if index + incr == len(i):
            total += prev_answer
            break
        operation = i[index + incr]
        incr += 1
        num, flag = i[index + incr], False
        while num.isnumeric():
            incr += 1
            if index + incr == len(i):
                flag = True
                break
            num += i[index + incr]
        num = int(num) if flag else int(num[:-1])
        incr -= 1
        if operation == '+':
            prev_answer += num
        else:
            prev_answer *= num
total_2 = 0      # part 2
for i in data:
    i = i.replace(' ', '')
    stack = deque()
    for j in range(len(i)):
        if i[j] == '(':
            stack.append(j)
    while stack:
        incr, index = 1, stack.pop()
        prev_answer = i[index + incr]
        while prev_answer.isnumeric():
            incr += 1
            prev_answer += i[index + incr]
        incr -= 1
        prev_answer, answers = int(prev_answer[:-1]), []
        while True:
            incr += 1
            operation = i[index + incr]
            if operation == ')':
                answers.append(prev_answer)
                product = 1
                for answer in answers:
                    product *= answer
                i = i[:index] + str(product) + i[i.find(')', index) + 1:]
                break
            incr += 1
            num = i[index + incr]
            while num.isnumeric():
                incr += 1
                num += i[index + incr]
            num = int(num[:-1])
            incr -= 1
            if operation == '*':
                answers.append(prev_answer)
                prev_answer = num
            else:
                prev_answer += num
    incr, index, prev_answer = 1, -1, i[0]
    while prev_answer.isnumeric():
        incr += 1
        prev_answer += i[index + incr]
    incr -= 1
    prev_answer = int(prev_answer[:-1])
    answers = []
    while True:
        incr += 1
        if index + incr == len(i):
            answers.append(prev_answer)
            product = 1
            for answer in answers:
                product *= answer
            total_2 += product
            break
        operation = i[index + incr]
        incr += 1
        num, flag = i[index + incr], False
        while num.isnumeric():
            incr += 1
            if index + incr == len(i):
                flag = True
                break
            num += i[index + incr]
        num = int(num) if flag else int(num[:-1])
        incr -= 1
        if operation == '*':
            answers.append(prev_answer)
            prev_answer = num
        else:
            prev_answer += num
print('Part 1: %d; part 2: %d' % (total, total_2))