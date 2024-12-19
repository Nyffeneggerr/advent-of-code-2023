import functools
from sympy import symbols, Eq, solve


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def parse_data(data):
    result = []
    current_game = {}

    for line_data in data:
        if "Button A" in line_data:
            amounts = line_data[10:].split(", ")
            current_game["A"] = [int(amounts[0][2:]), int(amounts[1][2:])]

        if "Button B" in line_data:
            amounts = line_data[10:].split(", ")
            current_game["B"] = [int(amounts[0][2:]), int(amounts[1][2:])]

        if "Prize" in line_data:
            amounts = line_data[7:].split(", ")
            current_game["Prize"] = [int(amounts[0][2:]) + 10_000_000_000_000, int(amounts[1][2:]) + 10_000_000_000_000]
            # current_game["Prize"] = [int(amounts[0][2:]), int(amounts[1][2:])]
            result.append(current_game)
            current_game = {}

    return result


if __name__ == '__main__':
    data = read_data()

    data = parse_data(data)

    coins = 0

    for game in data:
        a, b = symbols('a, b', integer=True)
        eq1 = Eq(a * game['A'][0] + b * game['B'][0], game['Prize'][0])
        eq2 = Eq(a * game['A'][1] + b * game['B'][1], game['Prize'][1])
        solution = solve((eq1, eq2))

        if solution:
            coins += solution[a] * 3 + solution[b]

        print(solution)

    print(coins)


    # a, b = symbols('a b')
    #
    # eq1 = Eq(data[0]['A'][0] * a + data[0]['B'][0], data[0]['Prize'][0])
    # eq2 = Eq(data[0]['A'][1] * a + data[0]['B'][1], data[0]['Prize'][1])
    #
    # solution = solve((eq1, eq2), (a, b))

    # a, b = symbols('a, b', integer=True)

    # eq1 = Eq(data[0]['A'][0] * a, data[0]['Prize'][0])
    # eq1 = Eq(a * 94 + b * 22, 8400)
    # eq2 = Eq(a * 34 + b * 67, 5400)
    # solution = solve((eq1, eq2))

    # print(solution)
