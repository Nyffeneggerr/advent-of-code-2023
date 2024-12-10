from pandas.core.ops import kleene_and


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def find_trailhead_and_append(row, col, num, data, trailheads):
    if num == 9:
        return 1

    new_num = num + 1

    total_paths = 0

    if row > 0:
        if int(data[row - 1][col]) == new_num:
            total_paths += find_trailhead_and_append(row - 1, col, new_num, data, trailheads)

    if row < len(data) - 1:
        if int(data[row + 1][col]) == new_num:
            total_paths += find_trailhead_and_append(row + 1, col, new_num, data, trailheads)

    if col > 0:
        if int(data[row][col - 1]) == new_num:
            total_paths += find_trailhead_and_append(row, col - 1, new_num, data, trailheads)

    if col < len(data[0]) - 1:
        if int(data[row][col + 1]) == new_num:
            total_paths += find_trailhead_and_append(row, col + 1, new_num, data, trailheads)

    return total_paths


def get_total_trailheads(row, col, data):
    trailheads = []

    return find_trailhead_and_append(row, col, 0, data, trailheads)


if __name__ == '__main__':
    data = read_data()

    total_trailheads = 0

    for row in range(len(data)):
        for col in range(len(data[0])):
            if int(data[row][col]) == 0:
                total_trailheads += get_total_trailheads(row, col, data)

    print(total_trailheads)
