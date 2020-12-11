def copy_seats(seats):
    return [
        row.copy() for row in seats
    ]


def fill_the_seats(seats, look_far_skip_floor=False, occupied_seat_limit=4):
    x = len(seats[0])
    y = len(seats)
    last_nr_occupied = 0
    while True:
        new_seats = copy_seats(seats)
        nr_occupied = 0
        for i in range(y):
            for j in range(x):
                seat = seats[i][j]
                nr_occupied_adjacent_seats = look_for_occupied_seats(seats, x, y, i, j, occupied_seat_limit,
                                                                     look_far_skip_floor)
                if seat == 'L' and nr_occupied_adjacent_seats == 0:
                    new_seats[i][j] = '#'
                elif seat == '#' and nr_occupied_adjacent_seats >= occupied_seat_limit:
                    new_seats[i][j] = 'L'

                if new_seats[i][j] == '#':
                    nr_occupied += 1

        if nr_occupied == last_nr_occupied:
            break
        else:
            last_nr_occupied = nr_occupied
        seats = copy_seats(new_seats)
    return last_nr_occupied


def look_for_occupied_seats(seats, xl, yl, x, y, occupied_seat_limit, look_far_skip_floor=False):
    nr_occupied_seats = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                # don't consider the seat we are sitting on
                continue

            ii = x + i
            jj = y + j
            while look_far_skip_floor and 0 <= ii < xl and 0 <= jj < yl and seats[ii][jj] == '.':
                # continue looking in the direction as long as it's only floor in the way
                ii += i
                jj += j
            if 0 <= ii < xl and 0 <= jj < yl and seats[ii][jj] == '#':
                nr_occupied_seats += 1

            if nr_occupied_seats >= occupied_seat_limit:
                # don't need to continue looking for occupied seats if we've reached 'occupied_seat_limit' or more
                # since it will trigger the # -> L regardless
                return nr_occupied_seats

    return nr_occupied_seats


def day11():
    with open('input.txt') as file:
        seats = [list(line.strip()) for line in file]

    print('part1', fill_the_seats(copy_seats(seats), occupied_seat_limit=4, look_far_skip_floor=False))
    print('part2', fill_the_seats(copy_seats(seats), occupied_seat_limit=5, look_far_skip_floor=True))


if __name__ == '__main__':
    day11()
