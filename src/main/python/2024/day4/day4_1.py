
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def next_pos(data, row, col):
    if row < 0:
        return ''

    if col < 0:
        return ''

    if row > len(data) - 1:
        return ''

    if col > len(data[0]) - 1:
        return ''

    return data[row][col]


if __name__ == '__main__':
    data = read_data()

    width = len(data[0])
    height = len(data)

    findings = 0

    for row in range(0, height):
        for col in range(0, width):
            if next_pos(data, row, col) == 'X':
                if next_pos(data, row, col - 1) == 'M':
                    if next_pos(data, row, col - 2) == 'A':
                        if next_pos(data, row, col - 3) == 'S':
                            findings += 1

                if next_pos(data, row - 1, col - 1) == 'M':
                    if next_pos(data, row - 2, col - 2) == 'A':
                        if next_pos(data, row - 3, col - 3) == 'S':
                            findings += 1

                if next_pos(data, row - 1, col) == 'M':
                    if next_pos(data, row - 2, col) == 'A':
                        if next_pos(data, row - 3, col) == 'S':
                            findings += 1

                if next_pos(data, row - 1, col + 1) == 'M':
                    if next_pos(data, row - 2, col + 2) == 'A':
                        if next_pos(data, row - 3, col + 3) == 'S':
                            findings += 1

                if next_pos(data, row, col + 1) == 'M':
                    if next_pos(data, row, col + 2) == 'A':
                        if next_pos(data, row, col + 3) == 'S':
                            findings += 1

                if next_pos(data, row + 1, col + 1) == 'M':
                    if next_pos(data, row + 2, col + 2) == 'A':
                        if next_pos(data, row + 3, col + 3) == 'S':
                            findings += 1

                if next_pos(data, row + 1, col) == 'M':
                    if next_pos(data, row + 2, col) == 'A':
                        if next_pos(data, row + 3, col) == 'S':
                            findings += 1

                if next_pos(data, row + 1, col - 1) == 'M':
                    if next_pos(data, row + 2, col - 2) == 'A':
                        if next_pos(data, row + 3, col - 3) == 'S':
                            findings += 1

    print(findings)
