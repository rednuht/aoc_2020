import math


def bin_search(search_path, n_min, n_max):
    while len(search_path) > 0:
        step = math.ceil((n_max - n_min) / 2)
        if search_path.pop(0) == 0:
            n_max -= step
        else:
            n_min += step
    return n_min


def day5():
    with open('input.txt') as file:
        boarding_passes = file.readlines()

    seat_map = dict()
    highest_seat_id = 0
    for boarding_pass in boarding_passes:
        boarding_pass = boarding_pass.strip()
        row_bin = [0 if c == 'F' else 1 for c in boarding_pass[0:7]]
        col_bin = [0 if c == 'L' else 1 for c in boarding_pass[7:]]

        row = bin_search(row_bin, 0, 127)
        col = bin_search(col_bin, 0, 7)
        seat_map.setdefault(row, []).append(col)
        seat_id = row * 8 + col
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print('part1', highest_seat_id)

    seat_set = {0, 1, 2, 3, 4, 5, 6, 7}
    for row, seats in seat_map.items():
        diff_seat = seat_set - set(seats)
        if len(diff_seat) == 1:
            print('part2', row * 8 + diff_seat.pop())
            break


if __name__ == '__main__':
    day5()
