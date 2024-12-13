import functools
import sys

sys.setrecursionlimit(1000000)


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
            current_game["Prize"] = [int(amounts[0][2:]), int(amounts[1][2:])]
            result.append(current_game)
            current_game = {}

    return result


@functools.cache
def move(x, y, use_cheap, cheap_x, cheap_y, expensive_x, expensive_y, dest_x, dest_y, token_count):
    if use_cheap:
        print("cheap")
        x += cheap_x
        y += cheap_y
    else:
        print("expensive")
        x += expensive_x
        y += expensive_y

    if x == dest_x and y == dest_y:
        print("found: " + str(token_count))
        return token_count

    if x > dest_x or y > dest_y:
        return 0

    cheap_token = move(x, y, True, cheap_x, cheap_y, expensive_x, expensive_y, dest_x, dest_y, token_count + 1)

    if cheap_token > 0:
        return cheap_token

    return move(x, y, False, cheap_x, cheap_y, expensive_x, expensive_y, dest_x, dest_y, token_count + 3)


def play_game_and_get_min_tokens(game):
    expensive = game["A"]
    cheap = game["B"]
    dest = game["Prize"]

    cheap_token = move(0, 0, True, cheap[0], cheap[1], expensive[0], expensive[1], dest[0], dest[1], 1)

    if cheap_token > 0:
        return cheap_token

    return move(0, 0, False, cheap[0], cheap[1], expensive[0], expensive[1], dest[0], dest[1], 3)


if __name__ == '__main__':
    data = read_data()

    data = parse_data(data)

    tokens = 0

    for game in data:
        token_returned = play_game_and_get_min_tokens(game)
        print(token_returned)
        tokens += token_returned

    print(data)
    print(tokens)
