data_dumps = []


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def north_cycle(data):
    rock_could_be_moved = True

    while(rock_could_be_moved):
        rock_could_be_moved = False

        for index, line in enumerate(data):
            if index > 0:
                for char_index in range(len(line)):
                    if line[char_index] == 'O':
                        if data[index-1][char_index] == '.':
                            data[index-1] = data[index-1][:char_index] + 'O' + data[index-1][char_index+1:]
                            data[index] = data[index][:char_index] + '.' + data[index][char_index+1:]
                            rock_could_be_moved = True


def west_cycle(data):
    rock_could_be_moved = True

    while(rock_could_be_moved):
        rock_could_be_moved = False

        for index, line in enumerate(data):
            for char_index in range(len(line)):
                if char_index > 0:
                    if line[char_index] == 'O' and line[char_index-1] == '.':
                        data[index] = data[index][:char_index-1] + 'O.' + data[index][char_index+1:]
                        rock_could_be_moved = True


def south_cycle(data):
    rock_could_be_moved = True

    while(rock_could_be_moved):
        rock_could_be_moved = False

        for index, line in enumerate(data):
            if index < len(data)-1:
                for char_index in range(len(line)):
                    if line[char_index] == 'O':
                        if data[index+1][char_index] == '.':
                            data[index+1] = data[index+1][:char_index] + 'O' + data[index+1][char_index+1:]
                            data[index] = data[index][:char_index] + '.' + data[index][char_index+1:]
                            rock_could_be_moved = True


def east_cycle(data):
    rock_could_be_moved = True

    while(rock_could_be_moved):
        rock_could_be_moved = False

        for index, line in enumerate(data):
            for char_index in range(len(line)):
                if char_index < len(line)-1:
                    if line[char_index] == 'O' and line[char_index+1] == '.':
                        data[index] = data[index][:char_index] + '.O' + data[index][char_index+2:]
                        rock_could_be_moved = True


def do_full_cycle(data):
    north_cycle(data)
    west_cycle(data)
    south_cycle(data)
    east_cycle(data)

    object_hash = hash(frozenset(data))

    if object_hash in data_dumps:
        data_dumps.clear()
        data_dumps.append(object_hash)
        return True

    data_dumps.append(object_hash)

    return False


if __name__ == '__main__':
    data = read_data()

    repeated = False
    cycle = 0
    repeated_first = 0
    repeated_second = 0

    while not repeated:
        if do_full_cycle(data):
            if repeated_first == 0:
                repeated_first = cycle
            else:
                if repeated_second == 0:
                    repeated_second = cycle
                    repeated = True
            # repeated = True
            print('Repeated at cycle: ' + str(cycle))

        cycle += 1

    distance = repeated_second - repeated_first

    print('Repeat distance: ' + str(distance))

    missing_cycles = (1_000_000_000 - cycle) % distance

    for x in range(missing_cycles):
        do_full_cycle(data)

    line_count = len(data)
    sum = 0

    for line in data:
        print(line)
        rock_count = line.count('O')
        sum += (rock_count * line_count)
        line_count -= 1

    print(sum)
