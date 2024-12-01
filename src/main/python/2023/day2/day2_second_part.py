

def read_games_from_file():
    with open('games.txt') as file:
        return [line.rstrip() for line in file]


def split_games_into_dict(games):
    games_dict = {}

    for game in games:
        first_game_split = game.split(':')
        game_number = first_game_split[0].split()[1]
        qube_sets = first_game_split[1].split(';')
        qubes = []

        for qube_set in qube_sets:
            qubes = qubes + qube_set.split(',')

        games_dict[game_number] = qubes

    return games_dict


def min_required_qubes_sum(qubes):
    lowest_pairs = {'red': 1, 'green': 1, 'blue': 1}

    for qube_entry in qubes:
        amount = int(qube_entry.split()[0])
        if 'red' in qube_entry:
            if amount > lowest_pairs['red']:
                lowest_pairs['red'] = amount

        if 'green' in qube_entry:
            if amount > lowest_pairs['green']:
                lowest_pairs['green'] = amount

        if 'blue' in qube_entry:
            if amount > lowest_pairs['blue']:
                lowest_pairs['blue'] = amount

    return lowest_pairs['red'] * lowest_pairs['green'] * lowest_pairs['blue']

def get_valid_games(games_dict):
    total_sum = 0

    for game_number in games_dict:
        total_sum += min_required_qubes_sum(games_dict[game_number])

    return total_sum


if __name__ == '__main__':
    games = read_games_from_file()
    # print(games)
    games_dict = split_games_into_dict(games)
    total_sum = get_valid_games(games_dict)
    print(total_sum)
