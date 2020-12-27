def get_next_int(i, largest=9):
    return i - 1 if i > 1 else largest


class Cup:
    def __init__(self, cup_nr):
        self.cup_nr = cup_nr
        self.next_cup = None

    def set_next(self, cup):
        self.next_cup = cup

    def find_destination(self, triplet_s, cup_map, largest=9):
        a = triplet_s.cup_nr
        b = triplet_s.next_cup.cup_nr
        c = triplet_s.next_cup.next_cup.cup_nr
        i = self.cup_nr
        while True:
            i = get_next_int(i, largest)
            if i != a and i != b and i != c:
                return cup_map[i]

    def detach_triplet(self):
        #              1          2       3
        third = self.next_cup.next_cup.next_cup
        first_after_triplet = third.next_cup
        third.next_cup = None
        first = self.next_cup
        self.next_cup = None

        return first, third, first_after_triplet

    def print_from_cup(self):
        return self.next_cup._print_from_cup(self.cup_nr, f'{self.cup_nr}')

    def _print_from_cup(self, starting_cup_nr, acc):
        if self.cup_nr == starting_cup_nr:
            return acc
        elif self.next_cup == None:
            return f'{acc}{self.cup_nr}'
        else:
            return self.next_cup._print_from_cup(starting_cup_nr, f'{acc}{self.cup_nr}')

    def __repr__(self):
        return f'{self.cup_nr}'

    def __str__(self):
        return f'{self.cup_nr}'


def part1(numbers):
    one_cup = None
    cup_map = dict()
    first_cup = Cup(numbers.pop(0))
    cup_map[first_cup.cup_nr] = first_cup
    last_cup = first_cup
    for number in reversed(numbers):
        cup = Cup(number)
        cup.set_next(last_cup)
        cup_map[number] = cup
        if number == 1:
            one_cup = cup
        last_cup = cup
    first_cup.set_next(last_cup)
    current_cup = first_cup

    for move in range(100):
        triplet_s, triplet_e, next_ = current_cup.detach_triplet()
        current_cup.set_next(next_)
        destination = current_cup.find_destination(triplet_s, cup_map)
        triplet_e.set_next(destination.next_cup)
        destination.set_next(triplet_s)
        current_cup = current_cup.next_cup

    print('part1', one_cup.print_from_cup()[1:])


def part2(numbers):
    cup_one = None
    largest = max(numbers)
    cup_map = dict()
    first_cup = Cup(numbers.pop(0))
    cup_map[first_cup.cup_nr] = first_cup
    last_cup = first_cup
    for number in numbers:
        cup = Cup(number)
        last_cup.set_next(cup)
        cup_map[number] = cup
        if number == 1:
            cup_one = cup
        last_cup = cup

    for number in range(largest + 1, 1000000 + 1):
        cup = Cup(number)
        last_cup.set_next(cup)
        cup_map[number] = cup
        last_cup = cup

    last_cup.set_next(first_cup)

    current_cup = first_cup
    for _ in range(10000000 - 1):
        triplet_s, triplet_e, next_ = current_cup.detach_triplet()
        current_cup.set_next(next_)
        destination = current_cup.find_destination(triplet_s, cup_map, largest=1000000)
        triplet_e.set_next(destination.next_cup)
        destination.set_next(triplet_s)
        current_cup = current_cup.next_cup

    print('part2', cup_one.next_cup.cup_nr * cup_one.next_cup.next_cup.cup_nr)


def day23():
    content = open('input.txt').read()

    numbers = [int(n) for n in list(content.strip())]
    part1(numbers.copy())
    part2(numbers.copy())


if __name__ == '__main__':
    day23()
