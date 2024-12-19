
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


if __name__ == '__main__':
    data = read_data()

    guards = parse_data(data)

    for i in range(100):
        for guard in guards:
            move_guard(guard)

    middle_row = int((rows - 1) / 2)
    middle_col = int((cols - 1) / 2)

    left_top = 0
    right_top = 0
    left_bottom = 0
    right_bottom = 0

    for guard in guards:
        x, y = guard['pos']

        if x < middle_col and y < middle_row:
            left_top += 1

        if x < middle_col and y > middle_row:
            left_bottom += 1

        if x > middle_col and y < middle_row:
            right_top += 1

        if x > middle_col and y > middle_row:
            right_bottom += 1

    result = left_top * right_top * left_bottom * right_bottom

    print(guards)
    print(result)
