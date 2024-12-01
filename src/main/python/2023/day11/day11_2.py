# factor = 999_999
factor = 9

def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def expand_the_map(data):
    y_max = len(data)
    x_max = len(data[0])

    columns = list(range(0, x_max))
    rows = list(range(0, y_max))

    for y in range(0, y_max):
        if '#' in data[y]:
            rows.remove(y)
        else:
            continue

        for x in columns:
            if '#' in data[y][x]:
                columns.remove(x)

    # print(columns)
    # print(rows)

    # new_max_x = x_max + len(columns)
    # new_max_y = y_max + len(rows)

    result_grid = list()

    for y in range(0, y_max):
        line = ''

        if y in rows:
            for count in range(0, factor):
                result_grid.append(''.ljust(x_max + (len(columns) * factor), '.'))

        for x in range(0, x_max):
            if x in columns:
                for count in range(0, factor):
                    line += '.'

            line += data[y][x]

        result_grid.append(line)

    for line in result_grid:
        print(line)

    return result_grid


if __name__ == '__main__':
    data = read_data()

    data = expand_the_map(data)

    galaxies = {}
    galaxy_counter = 0

    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if '#' in data[y][x]:
                galaxy_counter += 1
                galaxies[galaxy_counter] = [x,y]

    number_of_pairs = int(((galaxy_counter - 1) * galaxy_counter)/2)

    start_galaxy = 1
    total_distances = 0

    print(galaxies)

    for source_galaxy in range(1, galaxy_counter + 1):
        for destination_galaxy in range(source_galaxy + 1, galaxy_counter + 1):
            source_coords = galaxies[source_galaxy]
            dest_coords = galaxies[destination_galaxy]

            source_x = source_coords[0]
            source_y = source_coords[1]
            dest_x = dest_coords[0]
            dest_y = dest_coords[1]

            x_distance = dest_x - source_x if dest_x > source_x else source_x - dest_x
            y_distance = dest_y - source_y if dest_y > source_y else source_y - dest_y

            distance = x_distance + y_distance

            total_distances += distance

    print(total_distances)
