def day6():
    with open('input.txt') as file:
        content = file.read()

    nr_yes_part1 = 0
    nr_yes_part2 = 0
    for group in content.split('\n\n'):
        answer_map = dict()
        for person, questions in enumerate(group.split('\n')):
            for question in questions:
                answer_map.setdefault(person, set()).add(question)

        nr_yes_part1 += len(set.union(*answer_map.values()))
        nr_yes_part2 += len(set.intersection(*answer_map.values()))

    print('part1', nr_yes_part1)
    print('part2', nr_yes_part2)


if __name__ == '__main__':
    day6()
