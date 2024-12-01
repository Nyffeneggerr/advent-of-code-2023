

def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    data = read_data()

    left_list = []
    right_list = []

    for line in data:
        left_value, right_value = line.split('   ')
        left_list.append(int(left_value))
        right_list.append(int(right_value))

    result = 0

    for left_value in left_list:
        count = 0

        for right_value in right_list:
            if left_value == right_value:
                count += 1

        result += count * left_value

    print(result)