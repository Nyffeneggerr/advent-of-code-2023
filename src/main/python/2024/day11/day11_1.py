from mypyc.primitives.generic_ops import next_op


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    data = read_data()

    next_numbers = [int(x) for x in data[0].split(' ')]

    for x in range(25):
        result_list = []

        for i in range(len(next_numbers)):
            value = next_numbers[i]

            if value == 0:
                result_list.append(1)
            elif len(str(value)) % 2 == 0:
                str_value = str(value)
                center = int(len(str_value) / 2)
                value1 = int(str_value[:center])
                value2 = int(str_value[center:])
                result_list.append(value1)
                result_list.append(value2)
            else:
                result_list.append(value * 2024)

        next_numbers = result_list


    print(len(next_numbers))
