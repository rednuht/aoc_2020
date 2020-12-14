# stolen from:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Recursive_algorithm_2
def egcd(a: int, b: int):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = egcd(b_mod_a, a)
        return g, y - b_div_a * x, x


def modinv(a: int, b: int) -> int:
    """return x such that (x * a) % b == 1"""
    g, x, _ = egcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b


def part1(arrive_timestamp, bus_ids):
    timestamp = arrive_timestamp
    while True:
        departing_bus_id = None
        for bus_id in bus_ids:
            if bus_id == 'x':
                continue
            if timestamp % bus_id == 0:
                departing_bus_id = bus_id
                break
        if departing_bus_id is not None:
            break
        timestamp += 1
    print('part1', (timestamp - arrive_timestamp) * departing_bus_id)


def part2(bus_ids):
    congruences = []
    mod_product = 1
    for i, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            i %= bus_id
            congruences.append(((bus_id - i) % bus_id, bus_id))
            mod_product *= bus_id

    timestamp = 0
    for con, bus_id in congruences:
        ni = int(mod_product / bus_id)
        mi = modinv(ni, bus_id)
        timestamp += con * ni * mi

    result = timestamp % mod_product
    print('part2', result)


def day13():
    with open('input.txt') as file:
        lines = [line.strip() for line in file]

    arrive_timestamp = int(lines[0])
    bus_ids = [n if n == 'x' else int(n) for n in lines[1].split(',')]
    part1(arrive_timestamp, bus_ids)
    part2(bus_ids)


if __name__ == '__main__':
    day13()
