import itertools


def memory_address_combinations(number):
    floating_indices = []
    for i, c in enumerate(number):
        if c == 'X':
            floating_indices.append(i)

    for combinations in list(itertools.product([0, 1], repeat=len(floating_indices))):
        new_number = number
        for binary_value in combinations:
            new_number = new_number.replace('X', str(binary_value), 1)
        yield new_number


def solve(lines):
    memory_v1 = dict()
    memory_v2 = dict()
    mask = ''
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('mask'):
            mask = line.split()[-1]
        else:
            address_r, _, value_r = line.split(' ')
            address = address_r[4:-1]
            address_s = '{:036b}'.format(int(address))
            value = int(value_r)
            value_s = '{:036b}'.format(value)

            new_address = ''
            new_value = ''
            for j, c in enumerate(mask):
                if c == 'X':
                    new_address += c
                    new_value += value_s[j]
                elif c == '1':
                    new_address += c
                    new_value += c
                elif c == '0':
                    new_address += address_s[j]
                    new_value += c

            memory_v1[address] = int(new_value, 2)
            for memory_address in memory_address_combinations(new_address):
                memory_v2[memory_address] = value

    print('part1', sum(memory_v1.values()))
    print('part2', sum(memory_v2.values()))


def day14():
    with open('input.txt') as file:
        lines = [line.strip() for line in file]

    solve(lines)


if __name__ == '__main__':
    day14()
