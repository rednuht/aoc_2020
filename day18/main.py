import re

ops = {"+": (lambda x, y: x + y), "*": (lambda x, y: x * y)}
compute_1_pattern = re.compile(r'\(\d[\d+*]+\d\)')
compute_2_pattern = re.compile(r'\d+\+\d+')
compute_2_single_digit_pattern = re.compile(r'\((\d+)\)')


def substitute_fun(match):
    exp = match.group()
    if exp.startswith('(') and exp.endswith(')'):
        exp = exp[1:-1]

    return evaluate_exp(exp)


def evaluate_exp(exp):
    if len(exp) == 0:
        return ''

    exp = re.split(r'([+*])', exp)
    if len(exp) < 3:
        return ''.join(exp)

    s = int(exp[0])
    for i in range(1, len(exp) - 1, 2):
        s = ops[exp[i]](s, int(exp[i + 1]))
    return str(s)


def compute1(expression: str, once=False):
    while True:
        new_expression = compute_1_pattern.sub(substitute_fun, expression)
        if new_expression == expression or once:
            break
        expression = new_expression

    if once:
        return new_expression
    else:
        return evaluate_exp(expression)


def compute2(expression):
    while True:
        new_expression = compute_2_pattern.sub(substitute_fun, expression)
        new_expression = compute_2_single_digit_pattern.sub(r'\1', new_expression)

        if new_expression == expression and '+' in new_expression:
            new_expression = compute1(new_expression, once=True)
        elif new_expression == expression:
            break

        expression = new_expression

    return compute1(new_expression)


def day18():
    lines = open('input.txt').readlines()

    ans1 = 0
    ans2 = 0
    for line in lines:
        line = line.strip().replace(' ', '')
        ans1 += int(compute1(line))
        ans2 += int(compute2(line))

    print('part1', ans1)
    print('part2', ans2)


if __name__ == '__main__':
    day18()

# correct: 92173009047076
