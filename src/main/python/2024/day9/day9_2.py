from logilab.common.deprecation import moved


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

    print(result_array)
    read_idx = len(result_array) - 1
    moved_files = []

    could_move = True

    while could_move:
        print("another round...")
        could_move = False

        while read_idx > 0:
            read_value = result_array[read_idx]
            while read_value == '.':
                read_idx -= 1
                read_value = result_array[read_idx]

            read_value = int(read_value)

            file_size = 1
            read_idx -= 1

            if read_value in moved_files:
                # print("skipped: " + str(read_value))
                continue

            print(read_value)

            while (not result_array[read_idx] == '.') and read_value == int(result_array[read_idx]):
                file_size += 1
                read_idx -= 1

            found_gap_index = 0

            gap_size = 0
            this_time_first_gap = 0


            for x in range(read_idx):
                if result_array[x] == '.':
                    gap_size += 1

                    if gap_size == file_size:
                        found_gap_index = x - gap_size
                        break
                else:
                    gap_size = 0

            if found_gap_index > 0:
                could_move = True
                for x in range(file_size):
                    result_array[found_gap_index + x + 1] = read_value
                    result_array[read_idx + x + 1] = '.'

                moved_files.append(read_value)

            # print(result_array)

    result = 0

    for x in range(len(result_array)):
        if not result_array[x] == '.':
            result += (x * result_array[x])

    print(result_array)
    print(result)