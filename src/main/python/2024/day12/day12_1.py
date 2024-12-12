def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


garden_map = {}


def add_neighbour_fields(letter, row, col, data, garden_positions, all_scanned_fields):
    if row > 0:
        if not [row - 1, col] in all_scanned_fields:
            found_letter = data[row - 1][col]
            if found_letter == letter:
                garden_positions.append([row - 1, col])
                all_scanned_fields.append([row - 1, col])
                add_neighbour_fields(letter, row - 1, col, data, garden_positions, all_scanned_fields)

    if row < len(data) - 1:
        if not [row + 1, col] in all_scanned_fields:
            found_letter = data[row + 1][col]
            if found_letter == letter:
                garden_positions.append([row + 1, col])
                all_scanned_fields.append([row + 1, col])
                add_neighbour_fields(letter, row + 1, col, data, garden_positions, all_scanned_fields)

    if col > 0:
        if not [row, col - 1] in all_scanned_fields:
            found_letter = data[row][col - 1]
            if found_letter == letter:
                garden_positions.append([row, col - 1])
                all_scanned_fields.append([row, col - 1])
                add_neighbour_fields(letter, row, col - 1, data, garden_positions, all_scanned_fields)

    if col < len(data[0]) - 1:
        if not [row, col + 1] in all_scanned_fields:
            found_letter = data[row][col + 1]
            if found_letter == letter:
                garden_positions.append([row, col + 1])
                all_scanned_fields.append([row, col + 1])
                add_neighbour_fields(letter, row, col + 1, data, garden_positions, all_scanned_fields)


def add_map_entry(row, col, data, all_scanned_fields):
    letter = data[row][col]
    garden_positions = [[row, col]]
    all_scanned_fields.append([row, col])

    add_neighbour_fields(letter, row, col, data, garden_positions, all_scanned_fields)

    if letter in garden_map:
        garden_map[letter].append(garden_positions)
    else:
        garden_map[letter] = [garden_positions]



if __name__ == '__main__':
    data = read_data()
    all_scanned_fields = []

    for row in range(len(data)):
        for col in range(len(data[0])):
            if not [row, col] in all_scanned_fields:
                add_map_entry(row, col, data, all_scanned_fields)

    result = 0

    for key in garden_map.keys():
        for garden_fields in garden_map[key]:
            fences = 0

            for field in garden_fields:
                if not [field[0]-1, field[1]] in garden_fields:
                    fences += 1
                if not [field[0]+1, field[1]] in garden_fields:
                    fences += 1
                if not [field[0], field[1]-1] in garden_fields:
                    fences += 1
                if not [field[0], field[1]+1] in garden_fields:
                    fences += 1

            result += len(garden_fields) * fences


    print(garden_map)
    print(result)
