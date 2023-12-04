

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


def check_if_qubes_are_valid(qubes):
    for qube_entry in qubes:
        amount = int(qube_entry.split()[0])
        if "red" in qube_entry and amount > 12:
            return False

        if "green" in qube_entry and amount > 13:
            return False

        if "blue" in qube_entry and amount > 14:
            return False

    return True


def get_valid_games(games_dict):
    valid_games = []

    for game_number in games_dict:
        if check_if_qubes_are_valid(games_dict[game_number]):
            valid_games.append(game_number)

    return valid_games


if __name__ == '__main__':
    games = read_games_from_file()
    # print(games)
    games_dict = split_games_into_dict(games)
    valid_games = get_valid_games(games_dict)
    print(valid_games)
    print(sum([int(i) for i in valid_games]))
