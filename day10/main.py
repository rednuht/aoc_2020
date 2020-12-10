def part1(adapters):
    last_adapter_jolt = 0
    one_diffs = 0
    three_diffs = 0
    for adapter in adapters:
        if adapter - last_adapter_jolt == 1:
            one_diffs += 1
        elif adapter - last_adapter_jolt == 3:
            three_diffs += 1
        last_adapter_jolt = adapter

    print('part1', one_diffs * three_diffs)


def part2(adapters):
    arrangements = compute_adapter_chain_arrangements(0, set(adapters), {})
    print('part2', arrangements)


def compute_adapter_chain_arrangements(last_adapter, adapters, cache):
    next_adapters = {last_adapter + 1, last_adapter + 2, last_adapter + 3} & adapters
    if len(next_adapters) == 0:
        return 1

    if last_adapter in cache:
        return cache[last_adapter]

    ans = 0
    for next_adapter in next_adapters:
        ans += compute_adapter_chain_arrangements(next_adapter, adapters, cache)

    cache[last_adapter] = ans
    return ans


def day10():
    with open('input.txt') as file:
        adapters = sorted([int(line) for line in file])

    highest_adapter_jolt = adapters[-1]
    adapters.append(highest_adapter_jolt + 3)
    part1(adapters)
    part2(adapters)


if __name__ == '__main__':
    day10()
