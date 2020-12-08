import re

HCL_PATTERN = re.compile(r'#[a-f0-9]{6}')

key_validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: 59 <= int(x.split('in')[0]) <= 76 if 'in' in x else 150 <= int(x.split('cm')[0]) <= 193,
    'hcl': lambda x: HCL_PATTERN.match(x) is not None,
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: x is not None and len(x) == 9,
    'cid': lambda x: True,
}


def parse_passport(passport_raw):
    passport = dict()
    for pair in passport_raw.replace('\n', ' ').split():
        k, v = pair.split(':')
        passport[k] = v
    return passport


def day4():
    with open('input.txt') as file:
        content = file.read()

    valid_passports_part1 = 0
    valid_passports_part2 = 0
    for passport_raw in content.split('\n\n'):
        passport = parse_passport(passport_raw)

        if len(passport) == 8:
            valid_passports_part1 += 1
        elif len(passport) == 7 and 'cid' not in passport:
            valid_passports_part1 += 1

        if len(passport) >= 7:
            if all([key_validators[key](value) for key, value in passport.items()]):
                missing_keys = key_validators.keys() - passport.keys()
                if len(passport) == 8:
                    valid_passports_part2 += 1
                elif len(passport) == 7 and 'cid' in missing_keys:
                    valid_passports_part2 += 1

    print('part1', valid_passports_part1)
    print('part2', valid_passports_part2)


if __name__ == '__main__':
    day4()
