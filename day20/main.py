import math


def print_tile(tile):
    for row in tile:
        print(''.join(row).replace('.', ' '))


def tile_to_str(tile):
    s = ''
    for row in tile:
        s += ''.join(row) + '\n'
    return s


def rotate_tile(tile):
    # rotates tile 90° to the right
    return list(zip(*tile[::-1]))


def flip_tile(tile):
    return tile[::-1]


def get_opposite_direction(direction):
    if direction == 'N':
        return 'S'
    elif direction == 'S':
        return 'N'
    elif direction == 'E':
        return 'W'
    elif direction == 'W':
        return 'E'
    else:
        assert False


def sides_of_tile(tile):
    n = tile[0]
    s = tile[-1]
    e = []
    w = []
    for i in range(len(tile)):
        e.append(tile[i][0])
        w.append(tile[i][-1])

    return {
        'Nr': ''.join(n[::-1]),
        'N': ''.join(n),
        'Sr': ''.join(s[::-1]),
        'S': ''.join(s),
        'Er': ''.join(e[::-1]),
        'E': ''.join(e),
        'Wr': ''.join(w[::-1]),
        'W': ''.join(w)
    }


def get_side(tile, direction):
    if direction == 'N':
        return tile[0]
    elif direction == 'S':
        return tile[-1]
    elif direction == 'E':
        return [
            line[-1]
            for line in tile
        ]
    elif direction == 'W':
        return [
            line[0]
            for line in tile
        ]


def parse_tiles(content):
    blocks = content.split('\n\n')

    tiles_map = dict()
    for block in blocks:
        block = block.strip()
        if block == '':
            continue

        block_rows = block.split('\n')
        tile_nr_row = block_rows.pop(0)
        tile_nr = tile_nr_row.split()[-1][:-1]
        tile = []
        for block_row in block_rows:
            tile.append(list(block_row.strip()))

        tiles_map[int(tile_nr)] = tile

    return tiles_map


def get_monster_slices(tile):
    slices = []
    r_offset = 3
    c_offset = 20
    for i in range(0, len(tile) - r_offset):
        for j in range(0, len(tile) - c_offset):
            slice_ = [[], [], []]
            for r in range(3):
                for c in range(20):
                    slice_[r].append(tile[i + r][j + c])
            slices.append(slice_)

    return slices


def get_tile_combinations(tile):
    yield tile
    i = 0
    while i < 8:
        if i < 3:
            tile = rotate_tile(tile)
        elif i == 4:
            tile = rotate_tile(tile)
            tile = flip_tile(tile)
        elif i < 8:
            tile = rotate_tile(tile)
        else:
            tile = flip_tile(tile)
        yield tile
        i += 1


def compare_sides(sides1, sides2):
    return len(set(sides1) & set(sides2))


def combine_tiles(tiles_map, tiles_coordinates):
    size = int(math.sqrt(len(tiles_coordinates)))

    combined_tile = []
    for i in range(0, size):
        rows = [[] for _ in range(0, 8)]
        for j in range(0, size):
            tile_nr = tiles_coordinates[(i, j)]
            for n, r in enumerate(tiles_map[tile_nr]):
                if n == 0 or n == 9:
                    continue
                rows[n - 1] += r[1:-1]
        combined_tile += rows

    return combined_tile


def get_tile_to_neighbours(tiles_map):
    tile_nr_to_neighbours = dict()
    tile_nr_to_sides = {
        tile_nr: sides_of_tile(tile)
        for tile_nr, tile in tiles_map.items()
    }
    for tile_nr_f, tile_f in tiles_map.items():
        sides_tile_f = set(tile_nr_to_sides[tile_nr_f].values())
        tile_nrs_that_matches = []
        for tile_nr, sides in tile_nr_to_sides.items():
            if tile_nr_f == tile_nr:
                continue

            matches = compare_sides(sides_tile_f, sides.values())
            if matches > 0:
                tile_nrs_that_matches.append(tile_nr)
        tile_nr_to_neighbours[tile_nr_f] = tile_nrs_that_matches
    corners = [
        (tile_nr, neighbours)
        for tile_nr, neighbours in tile_nr_to_neighbours.items() if len(neighbours) == 2
    ]
    return corners, tile_nr_to_neighbours


def flip_rotate_to_fit(tile_map, tile_nr_fixed, tile_nr, direction):
    fixed_side = get_side(tile_map[tile_nr_fixed], direction)
    opposite_direction = get_opposite_direction(direction)
    i = 0
    while i < 9:
        side = get_side(tile_map[tile_nr], opposite_direction)
        if fixed_side == side:
            return True

        if i < 3:
            tile_map[tile_nr] = rotate_tile(tile_map[tile_nr])
        elif i == 4:
            tile_map[tile_nr] = rotate_tile(tile_map[tile_nr])
            tile_map[tile_nr] = flip_tile(tile_map[tile_nr])
        elif i < 8:
            tile_map[tile_nr] = rotate_tile(tile_map[tile_nr])
        else:
            tile_map[tile_nr] = flip_tile(tile_map[tile_nr])
        i += 1

    return False


def find_sea_monsters(combined_map):
    sea_monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]
    locations = []
    for i, row in enumerate(sea_monster):
        for j, char in enumerate(row):
            if char == '#':
                locations.append((i, j))

    for tile_combination in get_tile_combinations(combined_map):
        slices = get_monster_slices(tile_combination)
        nr_sea_monsters = 0
        for slice_ in slices:
            if all(slice_[i][j] == '#' for i, j in locations):
                nr_sea_monsters += 1

        if nr_sea_monsters > 0:
            return nr_sea_monsters, tile_combination

    return 0, []


def try_to_fit_tiles(tiles_map, size, tile_nr_to_neighbours, top_left_nr):
    current_tile_nr = top_left_nr
    tiles_coordinates = dict()
    placed_tiles = set()
    found_next = False
    for i in range(0, size):
        for j in range(0, size):
            neighbours = tile_nr_to_neighbours[current_tile_nr]
            alternatives = set(neighbours) - placed_tiles
            found_next = False
            if j == size - 1:
                tiles_coordinates[(i, j)] = current_tile_nr
                placed_tiles.add(current_tile_nr)
                found_next = True
            else:
                for tile_nr in alternatives:
                    if flip_rotate_to_fit(tiles_map, current_tile_nr, tile_nr, 'E'):
                        tiles_coordinates[(i, j)] = current_tile_nr
                        placed_tiles.add(current_tile_nr)
                        current_tile_nr = tile_nr
                        found_next = True
                        break

            if not found_next:
                break

        if not found_next:
            break

        first_tile_in_row = tiles_coordinates.get((i, 0), None)
        neighbours = tile_nr_to_neighbours.get(first_tile_in_row, [])
        alternatives = set(neighbours) - placed_tiles
        found_next = False

        if len(alternatives) == 0:
            found_next = True
        else:
            for tile_nr in alternatives:
                if flip_rotate_to_fit(tiles_map, first_tile_in_row, tile_nr, 'S'):
                    current_tile_nr = tile_nr
                    found_next = True
                    break

        if not found_next:
            break

    return found_next, tiles_coordinates


def part1(tiles_map):
    corners, _ = get_tile_to_neighbours(tiles_map)
    ans = 1
    for tile_nr, _ in corners:
        ans *= tile_nr

    print('part1', ans)


def part2(tiles_map):
    corners, tile_nr_to_neighbours = get_tile_to_neighbours(tiles_map)
    top_left_nr, _ = corners.pop(0)
    size = int(math.sqrt(len(tiles_map)))
    combinations = list(get_tile_combinations(tiles_map[top_left_nr]))
    while True:
        tiles_fitted, tiles_coordinates = try_to_fit_tiles(tiles_map, size, tile_nr_to_neighbours, top_left_nr)

        if tiles_fitted:
            break
        else:
            if len(combinations) > 0:
                tiles_map[top_left_nr] = combinations.pop(0)

        if len(combinations) == 0:
            if len(corners) == 0:
                assert False
            top_left_nr, _ = corners.pop(0)
            combinations = list(get_tile_combinations(tiles_map[top_left_nr]))

    combined_map = combine_tiles(tiles_map, tiles_coordinates)
    nr_sea_monsters, sea = find_sea_monsters(combined_map)
    print('part2', tile_to_str(sea).count('#') - nr_sea_monsters * 15)


def day20():
    content = open('input.txt').read()
    tiles_map = parse_tiles(content)

    part1(tiles_map)
    part2(tiles_map)


if __name__ == '__main__':
    day20()
