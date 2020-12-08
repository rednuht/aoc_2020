from functools import reduce


def traverse_map(length, tree_map, width, step_x, step_y):
    tree_pos = []
    open_pos = []
    x = 0
    y = 0
    while True:
        x = (x + step_x) % (width - 1)
        y += step_y
        if y >= length:
            break
        location = tree_map[y][x]
        if location == '.':
            open_pos.append((x, y))
        elif location == '#':
            tree_pos.append((x, y))
    return tree_pos, open_pos


def day3():
    with open('input.txt') as file:
        tree_map = file.readlines()

    length = len(tree_map)
    width = len(tree_map[0])
    step_options = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    num_trees_per_option = []
    for step_x, step_y, in step_options:
        tree_pos, _ = traverse_map(length, tree_map, width, step_x, step_y)
        num_trees_per_option.append(len(tree_pos))

    print('part1', num_trees_per_option[1])
    print('part2', reduce((lambda x, y: x * y), num_trees_per_option))


if __name__ == '__main__':
    day3()
