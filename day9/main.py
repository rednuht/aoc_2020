def check_part1(numbers, end_index, preamble_size=25):
    target = numbers[end_index]
    start_index = end_index - preamble_size
    for i in range(start_index, end_index - 1):
        for j in range(i + 1, end_index):
            if numbers[i] + numbers[j] == target:
                return True

    return False


def check_part2(numbers, target):
    numbers_size = len(numbers)
    start_index = 0
    while start_index < numbers_size - 2:
        target_sum = numbers[start_index] + numbers[start_index + 1]
        for i in range(start_index + 2, numbers_size):
            target_sum += numbers[i]
            if target_sum == target:
                sequence = sorted(numbers[start_index:i])
                return sequence[0] + sequence[-1]
            elif target_sum > target:
                start_index += 1
                break


def part1(numbers, preamble_size):
    invalid_number = 0
    for i in range(preamble_size, len(numbers)):
        if not check_part1(numbers, i, preamble_size=preamble_size):
            invalid_number = numbers[i]
            break

    print('part1', invalid_number)
    return invalid_number


def part2(numbers, invalid_number):
    print('part2', check_part2(numbers, invalid_number))


def day9():
    with open('input.txt') as file:
        numbers = [int(line) for line in file]

    preamble_size = 25
    invalid_number = part1(numbers, preamble_size)
    part2(numbers, invalid_number)


if __name__ == '__main__':
    day9()
