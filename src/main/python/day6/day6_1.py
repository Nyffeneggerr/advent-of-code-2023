
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_races(data):
    times = [int(x) for x in data[0][5:].split()]
    distances = [int(x) for x in data[1][10:].split()]
    races = []

    for number in range(len(times)):
        races.append([times[number], distances[number]])

    return races


def get_possible_wins_for_race(race):
    time = race[0]
    distance = race[1]
    win_count = 0

    for millis in range(1, time):
        if (millis * (time - millis)) > distance:
            win_count += 1

    return win_count


if __name__ == '__main__':
    data = read_data()

    races = get_races(data)
    print(races)
    possible_wins = []
    sum = 1

    for race in races:
        possible_wins.append(get_possible_wins_for_race(race))

    for possible_win in possible_wins:
        sum *= possible_win

    print(sum)
