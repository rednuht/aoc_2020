import timeit


def part1(nr_numbers, numbers):
    for i in range(0, nr_numbers):
        for j in range(i, nr_numbers):
            if numbers[i] + numbers[j] == 2020:
                print('part1', numbers[i] * numbers[j])
                return


def part2(nr_numbers, numbers):
    for i in range(0, nr_numbers):
        for j in range(i, nr_numbers):
            for k in range(j, nr_numbers):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print('part2', numbers[i] * numbers[j] * numbers[k])
                    return


def day1():
    with open('input.txt') as file:
        numbers = [int(n) for n in file]

    nr_numbers = len(numbers)
    numbers.sort()
    part1(nr_numbers, numbers)
    part2(nr_numbers, numbers)


if __name__ == '__main__':
    day1()
