
def read_data():
    with open('test_data.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    data = read_data()

    # testdata
    position = [6, 4, 1]
    # position = [94, 73]
    # directions: 1 = up, 2 = right, 3 = down, 4 = left
    # direction = 1
    visited = [position]

    while True:
        row = position[0]
        col = position[1]
        direction = position[2]

        if direction == 1:
            row -= 1
        if direction == 2:
            col +=1
        if direction == 3:
            row += 1
        if direction == 4:
            col -= 1

        if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]):
            break

        char_at_new_pos = data[row][col]

        if '.' in char_at_new_pos:
            new_position = [row , col, direction]
            if not new_position in visited:
                visited.append(new_position)
            position = new_position
        else:
            direction += 1
            if direction > 4:
                direction = 1
            position = [position[0], position[1], direction]

    result = len(visited)

    print(result)