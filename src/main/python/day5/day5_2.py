import re, sys


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_seeds(data):
    return [int(x) for x in data.pop(0)[7:].split()]


def fill_maplist(data):
    ongoing_map = False
    ongoing_list = []
    map_list = []

    for data_entry in data:
        if re.findall(":", data_entry):
            ongoing_map = True
        else:
            if data_entry == "":
                if ongoing_map:
                    ongoing_map = False
                    map_list.append(ongoing_list)
                    ongoing_list = []
            else:
                ongoing_list.append([int(x) for x  in data_entry.split()])

    map_list.append(ongoing_list)

    return map_list


def find_lowest_location(seeds, map_list):
    lowest_number = sys.maxsize
    start_seed = seeds[0]
    end_seed = start_seed + seeds[1]

    for seed in range(start_seed, end_seed):
        next_number = seed

        for map in map_list:
            found = False
            for register in map:
                if next_number >= register[1] and next_number < (register[1] + register[2]) and not found:
                    next_number = register[0] + (next_number - register[1])
                    found = True

        # print(f'Seed {seed} has location {next_number}')

        if next_number < lowest_number:
            lowest_number = next_number

    return lowest_number



if __name__ == '__main__':
    data = read_data()

    seeds = get_seeds(data)
    map_list = fill_maplist(data)
    print(find_lowest_location(seeds, map_list))
