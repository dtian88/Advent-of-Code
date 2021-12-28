from time import *
data = '#..#.' \
       '#.#.#' \
       '...#.' \
       '....#' \
       '#.#.#'

bugs = 0b1010110000010001010101001
# bugs = 0b0000100100110010100110000
# bugs = 0b0011011011101110111101001
empty = (1 << 25) - bugs - 1  # 0b0101001111101110101010110
shifts = [(0xF7BDEF, 1),  # left
          (0xFFFFF, 5),  # up
          (0x1EF7BDE, 1),  # right
          (0x1FFFFFF, 5)]  # down


def print_puzzle(bug):
    string_board = ''
    for x in range(5):
        for y in range(5):
            string_board += '# ' if bug & 1 else '. '
            bug >>= 1
        string_board += '\n'
    print(string_board[:-2])


def shift(board, direction):
    if direction < 2:  # rightward/downward shift
        return (board >> shifts[direction][1]) & shifts[direction][0]
    return (board << shifts[direction][1]) & shifts[direction][0]

t = perf_counter()
layouts = {bugs}
while True:
    bugs_alive = infested = 0
    bug_dirs = []
    empty_dirs = []
    for d in range(4):
        bug_dirs.append(shift(bugs, d) & bugs)
        # bugs_alive ^= shift(bugs, d) & bugs   # first attempt, didn't work
        empty_dirs.append(shift(bugs, d) & empty)
    (a, b, c, d) = bug_dirs     # hard-coded truth table
    bugs_alive = (a & ~b & ~c & ~d) | (~a & b & ~c & ~ d) | (~a & ~b & c & ~d) | (~a & ~b & ~c & d)
    (a, b, c, d) = empty_dirs
    infested = (a & ~b & ~c & ~d) | (~a & b & ~c & ~ d) | (~a & ~b & c & ~d) | (~a & ~b & ~c & d) | (
                a & b & ~c & ~d) | (a & ~b & c & ~d) | (a & ~b & ~c & d) | (~a & b & c & ~d) | (~a & b & ~c & d) | (
                           ~a & ~b & c & d)
    # for i in range(25):   # previous infested calculation involving a loop (working)
    #     count = 0
    #     for d in empty_dirs:
    #         if (1 << i) & d:
    #             count += 1
    #     if 1 <= count <= 2:
    #         infested |= 1 << i
    empty |= bugs ^ bugs_alive
    empty ^= infested
    bugs = bugs_alive | infested
    if bugs in layouts:
        break
    layouts.add(bugs)
print((perf_counter() - t) * 1000)
print_puzzle(bugs)
print()
print('Biodiversity rating: %d' % bugs)
