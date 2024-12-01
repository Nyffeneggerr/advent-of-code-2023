from collections import deque

from numpy.matlib import empty


def read_data():
    with open('data_result.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    data = read_data()

    result_list = list()
    counting_tiles = 0
    corner_chars = ['F', '7', 'J', 'L']

    for line in data:
        result_line = ''
        case = False
        last_corner = ''

        for char in line:
            if char == '|':
                case = not case
                result_line += char
            elif char in corner_chars:
                if last_corner == '':
                    last_corner = char
                else:
                    if last_corner == 'F' and char == 'J':
                        case = not case
                    elif last_corner == 'L' and char == '7':
                        case = not case
                    last_corner = ''

                result_line += char
            elif char == '.':
                if case:
                    result_line += '@'
                    counting_tiles += 1
                else:
                    result_line += '.'
            else:
                result_line += char

        result_list.append(result_line)

    with open('data_result_replaced.txt', 'w') as f:
        for line in result_list:
            f.write(f"{line}\n")

    print(result_list)
    print(counting_tiles)
