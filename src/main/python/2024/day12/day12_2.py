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


def check_if_fields_set(surround_fields, set_fields, ignore_fields):
    compare_fields = []
    for i in range(9):
        if i+1 in ignore_fields:
            compare_fields.append(surround_fields[i])
        elif i+1 == 5:
            compare_fields.append(True)
        else:
            compare_fields.append(i + 1 in set_fields)

    return compare_fields == surround_fields


def get_fences_for_field(s):
    # outer corner
    result = 0
    corners = 0
    if check_if_fields_set(s, [6 , 8], [1, 3, 7, 9]):
        corners += 1
        result += 1
    if check_if_fields_set(s, [4, 8], [1, 3, 9, 7]):
        corners += 1
        result += 1
    if check_if_fields_set(s, [2, 4], [1, 3, 7, 9]):
        corners += 1
        result += 1
    if check_if_fields_set(s, [2, 6], [1, 3, 7, 9]):
        corners += 1
        result += 1

    # inner corner
    if check_if_fields_set(s, [6 , 8], [1, 2, 3, 4, 7]):
        corners += 1
        result += 1
    if check_if_fields_set(s, [4, 8], [1, 2, 3, 6, 9]):
        corners += 1
        result += 1
    if check_if_fields_set(s, [2, 4], [3, 6, 7, 8, 9]):
        corners += 1
        result += 1
    if check_if_fields_set(s, [2, 6], [1, 4, 7, 8, 9]):
        corners += 1
        result += 1

    # # U shapes
    # if check_if_fields_set(s, [1, 3, 4, 6, 7, 8, 9], []):
    #     corners += 1
    #     result += 2
    # if check_if_fields_set(s, [1, 2, 3, 6, 7, 8, 9], []):
    #     corners += 1
    #     result += 2
    # if check_if_fields_set(s, [1, 2, 3, 4, 6, 7, 9], []):
    #     corners += 1
    #     result += 2
    # if check_if_fields_set(s, [1, 2, 3, 4, 7, 8, 9], []):
    #     corners += 1
    #     result += 2
    #
    # I shapes
    if check_if_fields_set(s, [2], [1, 3, 7, 9]):
        corners += 1
        result += 2
    if check_if_fields_set(s, [4], [1, 7, 3, 9]):
        corners += 1
        result += 2
    if check_if_fields_set(s, [8], [1, 3, 7, 9]):
        corners += 1
        result += 2
    if check_if_fields_set(s, [6], [1, 3, 7, 9]):
        corners += 1
        result += 2

    # Single field
    if check_if_fields_set(s, [], [1, 3, 7, 9]):
        corners = 0
        result = 4

    return [result, corners]


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
                surround_fields = [
                    [field[0]-1, field[1]-1] in garden_fields,
                    [field[0]-1, field[1]] in garden_fields,
                    [field[0]-1, field[1]+1] in garden_fields,
                    [field[0], field[1]-1] in garden_fields,
                    True,
                    [field[0], field[1]+1] in garden_fields,
                    [field[0]+1, field[1]-1] in garden_fields,
                    [field[0]+1, field[1]] in garden_fields,
                    [field[0]+1, field[1]+1] in garden_fields,
                ]

                field_fences, corners = get_fences_for_field(surround_fields)
                print("field: " + str(field) + " ,fences: " + str(field_fences) + ", corners: " + str(corners))

                fences += field_fences# - corners



                # field_fences = 0
                # if not [field[0]-1, field[1]] in garden_fields:
                #     field_fences += 1
                # if not [field[0]+1, field[1]] in garden_fields:
                #     field_fences += 1
                # if not [field[0], field[1]-1] in garden_fields:
                #     field_fences += 1
                # if not [field[0], field[1]+1] in garden_fields:
                #     field_fences += 1
                #
                # if field_fences == 0:
                #     continue
                #
                # if field_fences == 1:
                #     if [field[0]-1, field[1]-1] in garden_fields or [field[0]-1, field[1]+1] in garden_fields:
                #         field_fences += 1
                #
                #     if [field[0]+1, field[1]-1] in garden_fields or [field[0]+1, field[1]+1] in garden_fields:
                #         field_fences += 1
                #
                # if field_fences == 2:
                #     if [field[0]-1, field[1]-1] in garden_fields or [field[0]-1, field[1]+1] in garden_fields:
                #         field_fences += 1
                #
                #     if [field[0]+1, field[1]-1] in garden_fields or [field[0]+1, field[1]+1] in garden_fields:
                #         field_fences += 1
                #
                # if field_fences == 3:
                #     fences += 3
                #
                # if field_fences == 4:
                #     fences += 4

            # fences += 1

            print("letter: " + key + " / fences: " + str(fences))

            result += len(garden_fields) * fences


    print(garden_map)
    print(result)
