moves = {
    'e': lambda x, y, z: (x + 1, y - 1, z),
    'nw': lambda x, y, z: (x, y + 1, z - 1),
    'ne': lambda x, y, z: (x + 1, y, z - 1),
    'w': lambda x, y, z: (x - 1, y + 1, z),
    'sw': lambda x, y, z: (x - 1, y, z + 1),
    'se': lambda x, y, z: (x, y - 1, z + 1),
}


def get_adjacent_tiles(x, y, z):
    return {
        mover(x, y, z)
        for mover in moves.values()
    }


def color_count(tiles, coordinates):
    nr_black, nr_white = 0, 0
    for coordinate in coordinates:
        if coordinate not in tiles:
            continue
        if tiles[coordinate] == 'b':
            nr_black += 1
        else:
            nr_white += 1

    return nr_black, nr_white


def flip(color):
    if color == 'w':
        return 'b'
    else:
        return 'w'


def part1(lines):
    tiles = dict()
    for line in lines:
        i = 0
        x, y, z = 0, 0, 0
        while i < len(line):
            if i < len(line) - 1:
                a, b = line[i], line[i + 1]
            else:
                a, b = line[i], ''

            if f'{a}{b}' in moves:
                move = f'{a}{b}'
                i += 2
            else:
                move = a
                i += 1
            x, y, z = moves[move](x, y, z)

        if (x, y, z) in tiles:
            tiles[(x, y, z)] = flip(tiles[(x, y, z)])
        else:
            tiles[(x, y, z)] = 'b'

    nr_black = 0
    for _, color in tiles.items():
        if color == 'b':
            nr_black += 1

    print('part1', nr_black)

    return tiles


def part2(tiles):
    for day in range(100):
        tiles_c = tiles.copy()

        adjacent_tiles = set()
        for (x, y, z) in tiles.keys():
            adjacent_tiles |= get_adjacent_tiles(x, y, z)

        for coordinate in adjacent_tiles - set(tiles.keys()):
            tiles[coordinate] = 'w'

        for (x, y, z), color in tiles.items():
            nr_black, nr_white = color_count(tiles, get_adjacent_tiles(x, y, z))
            if color == 'b' and (nr_black == 0 or nr_black > 2):
                tiles_c[(x, y, z)] = 'w'
            elif color == 'w' and nr_black == 2:
                tiles_c[(x, y, z)] = 'b'

        tiles = tiles_c.copy()

    nr_black, _ = color_count(tiles, tiles.keys())
    print('part2', nr_black)


def day24():
    lines = [line.strip() for line in open('input.txt')]

    tiles = part1(lines)
    part2(tiles)


if __name__ == '__main__':
    day24()
