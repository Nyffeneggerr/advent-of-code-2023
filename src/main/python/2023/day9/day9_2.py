
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def find_next_value(data_line):
    current_values = [int(x) for x in data_line.split()]

    all_values_list = []
    all_values_list.append(current_values)

    while True:
        next_line_list = []

        for x in range(len(current_values)-1):
            next_value = current_values[x+1] - current_values[x]
            next_line_list.append(next_value)

        if sum(next_line_list) == 0:
            break

        all_values_list.append(next_line_list)

        current_values = next_line_list

    print(all_values_list)

    for x in range(len(all_values_list)-2, -1, -1):
        if x >= 0:
            current_list = all_values_list[x]
            previous_list = all_values_list[x+1]
            curent_next_value = current_list[0] - previous_list[0]
            all_values_list[x].insert(0, curent_next_value)

    return all_values_list[0][0]


if __name__ == '__main__':
    data = read_data()
    next_values = []

    for data_line in data:
        next_values.append(find_next_value(data_line))

    print(sum(next_values))
