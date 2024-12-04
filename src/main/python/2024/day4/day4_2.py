
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


def left_diagonal_valid(data, row ,col):
    if next_pos(data, row - 1, col - 1) == 'M':
        if next_pos(data, row + 1, col + 1) == 'S':
            return True

    if next_pos(data, row - 1, col - 1) == 'S':
        if next_pos(data, row + 1, col + 1) == 'M':
            return True

    return False


def right_diagonal_valid(data, row ,col):
    if next_pos(data, row - 1, col + 1) == 'M':
        if next_pos(data, row + 1, col - 1) == 'S':
            return True

    if next_pos(data, row - 1, col + 1) == 'S':
        if next_pos(data, row + 1, col - 1) == 'M':
            return True

    return False


if __name__ == '__main__':
    data = read_data()

    width = len(data[0])
    height = len(data)

    findings = 0

    for row in range(0, height):
        for col in range(0, width):
            if next_pos(data, row, col) == 'A':
                if left_diagonal_valid(data, row, col) and right_diagonal_valid(data, row, col):
                    findings += 1

    print(findings)
