
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    data = read_data()

    line = data[0]

    result_array = []
    file_id = 0

    defrag_array = []

    for x in range(len(line)):
        num = int(line[x])

        if x % 2 == 0:
            for i in range(num):
                result_array.append(file_id)

            file_id += 1
        else:
            for i in range(num):
                result_array.append('.')

    read_idx = len(result_array) - 1

    for x in range(len(result_array)):
        value = result_array[x]

        if x > read_idx:
            defrag_array = defrag_array[:x]
            break

        if value == '.':
            read_value = result_array[read_idx]
            while read_value == '.':
                read_idx -= 1
                read_value = result_array[read_idx]

            defrag_array.append(int(read_value))
            read_idx -= 1
        else:
            defrag_array.append(int(value))

    result = 0

    for x in range(len(defrag_array)):
        result += (x * defrag_array[x])

    print(result_array)
    print(defrag_array)
    print(result)
