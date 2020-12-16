def constraint_lambda_factory(a, b, c, d):
    return lambda x: a <= x <= b or c <= x <= d


def parse_constraints(constraints_r):
    constraints = dict()
    for line in constraints_r.split('\n'):
        key, key_constraints_r = line.split(': ')
        a, b, c, d = key_constraints_r.replace(' or ', '-').split('-')
        constraints[key] = constraint_lambda_factory(int(a), int(b), int(c), int(d))

    return constraints


def parse_nearby_tickets(nearby_tickets_r):
    nearby_tickets = [
        list(map(int, line.split(',')))
        for line in nearby_tickets_r.strip().split('\n')[1:]
    ]
    return nearby_tickets


def scan_nearby_tickets(constraints_map, nearby_tickets):
    ticket_scanning_error_rate = 0
    column_to_alternatives = {
        col: constraints_map.keys()
        for col in range(len(nearby_tickets[0]))
    }
    for nearby_ticket in nearby_tickets:
        is_invalid = False
        number_valid_map = dict()
        for i, number in enumerate(nearby_ticket):
            valid_fields = {key: validator(number) for key, validator in constraints_map.items()}
            number_valid_map[i] = valid_fields
            if not any(valid_fields.values()):
                is_invalid = True
                ticket_scanning_error_rate += number

        if not is_invalid:
            for col, type_valid_map in number_valid_map.items():
                not_valid_types = {type_ for type_, valid in type_valid_map.items() if not valid}
                column_to_alternatives[col] -= not_valid_types
    return column_to_alternatives, ticket_scanning_error_rate


def reduce_ticket_field_alternatives(column_to_alternatives):
    taken_types = set()
    while True:
        all_determined = True
        for alternatives in column_to_alternatives.values():
            if len(alternatives) == 1:
                taken_types |= alternatives
            else:
                all_determined = False
                alternatives -= taken_types
        if all_determined:
            break


def compute_departure_fields_product(column_to_alternatives, my_ticket_numbers):
    departure_field_value_product = 1
    for col, alternatives in column_to_alternatives.items():
        if list(alternatives)[0].startswith('departure'):
            departure_field_value_product *= my_ticket_numbers[col]
    return departure_field_value_product


def day16():
    content = open('input.txt').read()

    constraints_r, my_ticket_r, nearby_tickets_r = content.split('\n\n')

    constraints_map = parse_constraints(constraints_r)
    my_ticket_numbers = list(map(int, my_ticket_r.split('\n')[-1].split(',')))
    nearby_tickets = parse_nearby_tickets(nearby_tickets_r)

    column_to_alternatives, ticket_scanning_error_rate = scan_nearby_tickets(constraints_map, nearby_tickets)
    reduce_ticket_field_alternatives(column_to_alternatives)
    departure_fields_value_product = compute_departure_fields_product(column_to_alternatives, my_ticket_numbers)

    print('part1', ticket_scanning_error_rate)
    print('part2', departure_fields_value_product)


if __name__ == '__main__':
    day16()
