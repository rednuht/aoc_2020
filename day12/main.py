import math


def parse_nav_instructions(nav_instructions):
    for instruction in nav_instructions:
        yield instruction[0], int(instruction[1:])


def part1(nav_instructions):
    direction = 0
    ship_x = 0
    ship_y = 0
    for action, value in parse_nav_instructions(nav_instructions):
        if action == 'N':
            ship_y += value
        elif action == 'S':
            ship_y -= value
        elif action == 'E':
            ship_x += value
        elif action == 'W':
            ship_x -= value
        elif action == 'L':
            direction = (direction + value) % 360
        elif action == 'R':
            direction = (direction - value) % 360
        elif action == 'F':
            if direction == 0:
                # east
                ship_x += value
            elif direction == 90:
                # north
                ship_y += value
            elif direction == 180:
                # west
                ship_x -= value
            elif direction == 270:
                # south
                ship_y -= value
    print('part1', abs(ship_x) + abs(ship_y))


def part2(nav_instructions):
    waypoint_x = 10
    waypoint_y = 1
    ship_x = 0
    ship_y = 0
    for action, value in parse_nav_instructions(nav_instructions):
        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'L' or action == 'R':
            # rotate the waypoint
            # x' = x*cos(rads) - y*sin(rads)
            # y' = y*cos(rads) + x*sin(rads)
            rads = math.radians(value)
            if action == 'R':
                rads *= -1
            new_waypoint_x = waypoint_x * math.cos(rads) - waypoint_y * math.sin(rads)
            new_waypoint_y = waypoint_y * math.cos(rads) + waypoint_x * math.sin(rads)
            waypoint_x = round(new_waypoint_x)
            waypoint_y = round(new_waypoint_y)
        elif action == 'F':
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value

    print('part2', abs(ship_x) + abs(ship_y))


def day12():
    with open('input.txt') as file:
        lines = [line.strip() for line in file]

    part1(lines)
    part2(lines)


if __name__ == '__main__':
    day12()
