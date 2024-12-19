
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


# rows = 7
# cols = 11
rows = 103
cols = 101


def parse_data(data):
    result = []

    for line in data:
        parts = line.split(' ')
        pos = [int(x) for x in parts[0][2:].split(',')]
        vel = [int(x) for x in parts[1][2:].split(',')]
        result.append({'pos': pos, 'vel': vel})

    return result


def move_guard(guard):
    vel = guard['vel']
    pos = guard['pos']

    new_x = pos[0] + vel[0]
    new_y = pos[1] + vel[1]

    if new_x >= cols:
        new_x -= cols

    if new_x < 0:
        new_x += cols

    if new_y >= rows:
        new_y -= rows

    if new_y < 0:
        new_y += rows

    guard['pos'] = [new_x, new_y]

    return new_y, new_x


if __name__ == '__main__':
    data = read_data()

    guards = parse_data(data)

    i = 0

    while i < 10_000_000_000:
        i += 1

        if (i - 64) % 103 != 0:
            for guard in guards:
                move_guard(guard)
        else:
            row_nums = {}
            col_nums = {}

            for guard in guards:
                row, col = move_guard(guard)

                if row in row_nums:
                    row_nums[row] = row_nums[row] + 1
                else:
                    row_nums[row] = 1

                if col in col_nums:
                    col_nums[col] = col_nums[col] + 1
                else:
                    col_nums[col] = 1

            max_row_count = 0
            for row in row_nums.values():
                if row > max_row_count:
                    max_row_count = row

            max_col_count = 0
            for col in col_nums.values():
                if col > max_col_count:
                    max_col_count = col

            if max_row_count > 25 and max_col_count > 25:
                print('Max row count at second: ' + str(max_row_count) + ' / ' + str(i))
                print('Max col count at second: ' + str(max_col_count) + ' / ' + str(i))

            if i == 7892:
                break

    positions = [guard['pos'] for guard in guards]

    grid = []

    for i in range(rows):
        grid_row = ''

        for x in range(cols):
            if [x, i] in positions:
                grid_row += '*'
            else:
                grid_row += '.'

        grid.append(grid_row)

    print(positions)

    for row in grid:
        print(row)
