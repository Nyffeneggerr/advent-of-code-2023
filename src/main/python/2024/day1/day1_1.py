

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

    left_list.sort()
    right_list.sort()

    result = 0

    for i in range(0, len(left_list)):
        result += abs(left_list[i] - right_list[i])

    print(result)