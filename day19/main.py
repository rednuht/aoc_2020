import re


def lambda_base_factory(rest):
    return lambda: rest[1]


def lambda_or_factory(rule_map, rest):
    return lambda: '(' + '|'.join([
        lambda_and_factory(rule_map, part)()
        for part in rest.split(' | ')
    ]) + ')'


def lambda_and_factory(rule_map, rest):
    return lambda: ''.join([
        rule_map[int(id_)]()
        for id_ in rest.split()
    ])


def parse_rules(rules_s):
    rule_map = dict()
    for rule_r in rules_s.split('\n'):
        rule_nr, rest = rule_r.split(': ')
        rule_nr = int(rule_nr)
        if '"' in rest:
            rule_map[rule_nr] = lambda_base_factory(rest)
        elif '|' in rest:
            rule_map[rule_nr] = lambda_or_factory(rule_map, rest)
        else:
            rule_map[rule_nr] = lambda_and_factory(rule_map, rest)

    return rule_map


def part1(rule_map, messages):
    pattern = re.compile(rule_map[0]())
    ans = 0
    for a in messages:
        m = pattern.fullmatch(a)
        if m is not None:
            ans += 1

    print('part1', ans)


def part2(rule_map, messages):
    p_42 = rule_map[42]()
    p_31 = rule_map[31]()
    n = 2

    def eight_rule_special():
        return '(' + '|'.join([
            ''.join([
                rule_map[int(id_)]() if int(id_) != 8 else f'({p_42}+)'
                for id_ in part.split()
            ])
            for part in '42 | 42 8'.split(' | ')
        ]) + ')'

    def eleven_rule_special():
        return '(' + '|'.join([
            ''.join([
                rule_map[int(id_)]()
                if int(id_) != 11
                else '(' + '|'.join([f'{p_42}{{{i}}}{p_31}{{{i}}}' for i in range(1, n)]) + ')'
                for id_ in part.split()
            ])
            for part in '42 31 | 42 11 31'.split(' | ')
        ]) + ')'

    rule_map[8] = eight_rule_special
    rule_map[11] = eleven_rule_special
    prev_ans = 0
    while True:
        pattern = re.compile(rule_map[0]())
        ans = 0
        for a in messages:
            m = pattern.fullmatch(a)
            if m is not None:
                ans += 1

        if prev_ans == ans:
            break

        print(ans)
        n += 1
        prev_ans = ans

    print('part2', ans)


def day19():
    content = open('input.txt').read()

    rules_s, messages_s = content.split('\n\n')
    messages = messages_s.split('\n')
    rule_map = parse_rules(rules_s)

    part1(rule_map, messages)
    part2(rule_map, messages)


if __name__ == '__main__':
    day19()
