def adjacent_coordinates(r_min, r_max, hyper=False):
    for x in range(r_min, r_max + 1):
        for y in range(r_min, r_max + 1):
            for z in range(r_min, r_max + 1):
                if hyper:
                    for w in range(r_min, r_max + 1):
                        yield x, y, z, w
                else:
                    yield x, y, z


def get_adjacent_coordinates_of_coordinate(x, y, z, w=0, hyper=False):
    for c in adjacent_coordinates(-1, 1, hyper=hyper):
        if hyper:
            xx, yy, zz, ww = c
            yield x + xx, y + yy, z + zz, w + ww
        else:
            xx, yy, zz = c
            yield x + xx, y + yy, z + zz


def part1(active_cubes):
    for _ in range(6):
        new_active_cubes = set()
        for x, y, z in [c for x, y, z in active_cubes for c in get_adjacent_coordinates_of_coordinate(x, y, z)]:
            nr_adjacent_active = 0
            for xx, yy, zz in adjacent_coordinates(-1, 1):
                if (xx != 0 or yy != 0 or zz != 0) and (x + xx, y + yy, z + zz) in active_cubes:
                    nr_adjacent_active += 1
                if nr_adjacent_active > 3:
                    break

            if (nr_adjacent_active in [2, 3] and (x, y, z) in active_cubes) or \
                    (nr_adjacent_active == 3 and (x, y, z) not in active_cubes):
                new_active_cubes.add((x, y, z))

        active_cubes = new_active_cubes

    print('part1', len(active_cubes))


def part2(active_cubes):
    # add 4th dimension
    active_cubes = {
        (x, y, z, 0)
        for x, y, z in active_cubes
    }
    for _ in range(6):
        new_active_cubes = set()
        for x, y, z, w in [c for x, y, z, w in active_cubes for c in
                           get_adjacent_coordinates_of_coordinate(x, y, z, w, hyper=True)]:
            nr_adjacent_active = 0
            for xx, yy, zz, ww in adjacent_coordinates(-1, 1, hyper=True):
                if (xx != 0 or yy != 0 or zz != 0 or ww != 0) and (x + xx, y + yy, z + zz, w + ww) in active_cubes:
                    nr_adjacent_active += 1
                if nr_adjacent_active > 3:
                    break

            if (nr_adjacent_active in [2, 3] and (x, y, z, w) in active_cubes) or \
                    (nr_adjacent_active == 3 and (x, y, z, w) not in active_cubes):
                new_active_cubes.add((x, y, z, w))

        active_cubes = new_active_cubes

    print('part2', len(active_cubes))


def day17():
    content = open('input.txt').read()

    lines = content.strip().split('\n')
    initial_active_cubes = {
        (x, y, 0)
        for y, line in enumerate(lines) for x, cube in enumerate(line) if cube == '#'
    }
    part1(initial_active_cubes.copy())
    part2(initial_active_cubes)


if __name__ == '__main__':
    day17()
