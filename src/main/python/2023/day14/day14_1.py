
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    data = read_data()

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

    line_count = len(data)
    sum = 0

    for line in data:
        rock_count = line.count('O')
        sum += (rock_count * line_count)
        line_count -= 1

    print(sum)
