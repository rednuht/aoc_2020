def part1(player1, player2):
    while True:
        if len(player1) == 0 or len(player2) == 0:
            winner = player1 if len(player2) == 0 else player2
            break

        a = player1.pop(0)
        b = player2.pop(0)

        if a > b:
            player1 += [a, b]
        else:
            player2 += [b, a]

    score = sum((i + 1) * n for i, n in enumerate(reversed(winner)))
    print('part1', score)


def recursive_combat(player1, player2):
    memory = set()
    while True:
        if (tuple(player1), tuple(player2)) in memory:
            return True, player1

        memory.add((tuple(player1), tuple(player2)))
        if len(player1) == 0 or len(player2) == 0:
            winner, player1_wins = (player1, True) if len(player2) == 0 else (player2, False)
            break

        a = player1.pop(0)
        b = player2.pop(0)

        if len(player1) >= a and len(player2) >= b:
            player1_wins, _ = recursive_combat(player1[:a], player2[:b])
        else:
            player1_wins = a > b

        if player1_wins:
            player1 += [a, b]
        else:
            player2 += [b, a]

    return player1_wins, winner


def part2(player1, player2):
    _, winner_deck = recursive_combat(player1, player2)
    print('part2', sum((i + 1) * n for i, n in enumerate(reversed(winner_deck))))


def day22():
    content = open('input.txt').read()

    player1_r, player2_r = content.split('\n\n')

    def parse_player(player_number_str):
        return [int(n) for n in player_number_str.strip().split('\n')[1:]]

    player1 = parse_player(player1_r)
    player2 = parse_player(player2_r)

    part1(player1.copy(), player2.copy())
    part2(player1, player2)


if __name__ == '__main__':
    day22()
