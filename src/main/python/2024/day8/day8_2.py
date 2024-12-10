def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def calculate_antinode_positions(antenna1, antenna2, row_max, col_max):
    result = [antenna1, antenna2]

    x_dist = antenna2[0] - antenna1[0]
    y_dist = abs(antenna1[1] - antenna2[1])

    if antenna1[1] < antenna2[1]:
        x = antenna1[0] - x_dist
        y = antenna1[1] - y_dist
        while 0 <= x < row_max and 0 <= y < col_max:
            result.append([x, y])
            x -= x_dist
            y -= y_dist

        x = antenna2[0] + x_dist
        y = antenna2[1] + y_dist
        while 0 <= x < row_max and 0 <= y < col_max:
            result.append([x, y])
            x += x_dist
            y += y_dist
    else:
        x = antenna1[0] - x_dist
        y = antenna1[1] + y_dist
        while 0 <= x < row_max and 0 <= y < col_max:
            result.append([x, y])
            x -= x_dist
            y += y_dist

        x = antenna2[0] + x_dist
        y = antenna2[1] - y_dist
        while 0 <= x < row_max and 0 <= y < col_max:
            result.append([x, y])
            x += x_dist
            y -= y_dist

    return result


if __name__ == '__main__':
    data = read_data()

    position_map = {}

    col_max = len(data[0])
    row_max = len(data)

    for row in range(len(data)):
        for col in range(len(data[0])):
            value = data[row][col]
            if not value == '.':
                if value in position_map:
                    list_in_list = position_map[value]
                    list_in_list.append([row, col])
                    position_map[value] = list_in_list
                else:
                    position_map[value] = [[row, col]]

    valid_positions = []

    for key in position_map.keys():
        antenna_positions = position_map[key]

        for x in range(len(antenna_positions)):
            for i in range(x + 1, len(antenna_positions)):
                antinode_positions = calculate_antinode_positions(antenna_positions[x], antenna_positions[i], row_max, col_max)

                for pos in antinode_positions:
                    if not pos in valid_positions:
                        valid_positions.append(pos)

    # print(defrag_array)
    print(position_map)
    print(len(valid_positions))

