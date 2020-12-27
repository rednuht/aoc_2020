def transform_subject_number(loop_size, subject_number):
    return pow(subject_number, loop_size, mod=20201227)


def find_loop_size(target):
    value = 1
    loop_size = 0

    while value != target:
        value = value * 7 % 20201227
        loop_size += 1

    return loop_size


def day25():
    public_keys = [int(line.strip()) for line in open('input.txt')]

    print('part1', transform_subject_number(find_loop_size(public_keys[1]), public_keys[0]))


if __name__ == '__main__':
    day25()
