if __name__ == '__main__':
    data = "27 10647 103 9 0 5524 4594227 902936"
    next_numbers = [int(x) for x in data[0].split(' ')]

    for x in range(75):
        print("Run: " + str(x))
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
