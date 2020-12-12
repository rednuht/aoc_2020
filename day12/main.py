import math

NAV_MAP = {
    'N': [0, 1],
    'S': [0, -1],
    'E': [1, 0],
    'W': [-1, 0],
}


def parse_nav_instructions(nav_instructions):
    for instruction in nav_instructions:
        yield instruction[0], int(instruction[1:])


def part1(nav_instructions):
    direction = 0
    ship_x = 0
    ship_y = 0
    dir_map = {
        0: [1, 0],
        90: [0, 1],
        180: [-1, 0],
        270: [0, -1],
    }
    for action, value in parse_nav_instructions(nav_instructions):
        if action == 'L':
            direction = (direction + value) % 360
        elif action == 'R':
            direction = (direction - value) % 360
        elif action == 'F':
            ship_x += dir_map[direction][0] * value
            ship_y += dir_map[direction][1] * value
        else:
            ship_x += NAV_MAP[action][0] * value
            ship_y += NAV_MAP[action][1] * value

    print('part1', abs(ship_x) + abs(ship_y))


def part2(nav_instructions):
    waypoint_x = 10
    waypoint_y = 1
    ship_x = 0
    ship_y = 0
    for action, value in parse_nav_instructions(nav_instructions):
        if action == 'L' or action == 'R':
            # rotate the waypoint
            # (waypoint_x + waypoint_y*i) * (-)i will rotate by +/- pi/2
            i = complex(0, 1 if action == 'L' else -1)
            c = complex(waypoint_x, waypoint_y)
            for _ in range(int(value / 90)):
                c *= i

            waypoint_x = c.real
            waypoint_y = c.imag
        elif action == 'F':
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value
        else:
            waypoint_x += NAV_MAP[action][0] * value
            waypoint_y += NAV_MAP[action][1] * value

    print('part2', int(abs(ship_x) + abs(ship_y)))


def day12():
    with open('input.txt') as file:
        lines = [line.strip() for line in file]

    part1(lines)
    part2(lines)


if __name__ == '__main__':
    day12()
