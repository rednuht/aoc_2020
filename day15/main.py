from tqdm import tqdm


def day15():
    numbers = [int(n) for n in open('input.txt').read().split(',')]

    part1 = -1
    memory = dict()
    last_number = None
    number = -1
    for turn, n in enumerate(numbers):
        last_number = n
        memory[last_number] = turn + 1

    for turn in tqdm(range(len(numbers), 30000000)):
        if last_number in memory:
            number = turn - memory[last_number]
        else:
            number = 0

        memory[last_number] = turn
        if turn == 2020:
            part1 = last_number
        last_number = number
        turn += 1

    print('part1', part1)
    print('part2', number)


if __name__ == '__main__':
    day15()
