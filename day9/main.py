def check_part1(numbers, end_index, preamble_size=25):
    target = numbers[end_index]
    start_index = end_index - preamble_size
    for i in range(start_index, end_index):
        for j in range(i, end_index):
            if numbers[i] + numbers[j] == target:
                return True

    return False


def check_part2(numbers, target):
    numbers_size = len(numbers)
    start_index = 0
    target_sum = 0
    while start_index < numbers_size:
        for i in range(start_index, numbers_size):
            number = numbers[i]
            target_sum += number
            if target_sum == target:
                sequence = numbers[start_index:i]
                return min(sequence) + max(sequence)
            elif target_sum > target:
                target_sum = 0
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
