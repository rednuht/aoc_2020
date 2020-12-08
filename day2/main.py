class Policy:
    def __init__(self, policy):
        condition_raw, letter = policy.split()
        self.letter = letter
        a, b = condition_raw.split('-')
        self.a = int(a)
        self.b = int(b)

    def is_password_valid_part1(self, password):
        return self.a <= password.count(self.letter) <= self.b

    def is_password_valid_part2(self, password):
        pos1 = password[self.a - 1] == self.letter
        pos2 = password[self.b - 1] == self.letter
        return pos1 ^ pos2


def day2():
    with open('input.txt') as file:
        lines = file.readlines()

    part1_valid_passwords = 0
    part2_valid_passwords = 0
    for line in lines:
        policy_str, password = line.split(':')
        policy = Policy(policy_str)
        password = password.strip()
        if policy.is_password_valid_part1(password):
            part1_valid_passwords += 1
        if policy.is_password_valid_part2(password):
            part2_valid_passwords += 1

    print('part1', part1_valid_passwords)
    print('part2', part2_valid_passwords)


if __name__ == '__main__':
    day2()
