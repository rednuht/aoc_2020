import re


class Bag:
    def __init__(self, color, rules):
        self.color = color
        self.rules = rules

    def __hash__(self) -> int:
        return hash(self.color)

    def __eq__(self, other):
        return self.color == other.color

    def fill_bag_rules_placeholders(self, bags_map):
        self.rules = {
            bags_map[bag_color]: quantity
            for bag_color, quantity in self.rules.items()
        }

    def bags_in_bags(self, multiplier=1):
        return self._bags_in_bags(multiplier, 0)

    def _bags_in_bags(self, multiplier, acc):
        for sub_bag, quantity in self.rules.items():
            acc += sub_bag.bags_in_bags(quantity * multiplier)
            acc += quantity * multiplier

        return acc

    def search_bag(self, target_color, acc=False):
        return self._search_bag(target_color, acc)

    def _search_bag(self, target_color, acc):
        for sub_bag, quantity in self.rules.items():
            if sub_bag.color == target_color:
                acc = True
            else:
                acc = sub_bag.search_bag(target_color, acc)

        return acc


def part1(bags):
    can_contain_shiny_gold_bag = 0
    for bag in bags:
        if bag.search_bag('shiny gold'):
            can_contain_shiny_gold_bag += 1
    print('part1', can_contain_shiny_gold_bag)


def part2(shiny_gold_bag):
    nr_bags_in_shiny_gold_bag = shiny_gold_bag.bags_in_bags()
    print('part2', nr_bags_in_shiny_gold_bag)


def parse_lines(lines):
    bags = []
    bags_map = dict()
    bags_pattern = re.compile(r'(\d+) (\w+ \w+)')

    for line in lines:
        main_bag_color, rest = line.split(' bags', 1)
        bag_rules = {
            bag_color: int(quantity)
            for quantity, bag_color in bags_pattern.findall(rest)
        }

        bag = Bag(main_bag_color, bag_rules)
        bags.append(bag)
        bags_map[main_bag_color] = bag

    for bag in bags:
        bag.fill_bag_rules_placeholders(bags_map)

    return bags, bags_map


def day7():
    with open('input.txt') as file:
        lines = file.readlines()

    bags, bags_map = parse_lines(lines)

    part1(bags)
    part2(bags_map['shiny gold'])


if __name__ == '__main__':
    day7()
