
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_value_for_string(string):
    sum = 0

    for x in range(len(string)):
        char = string[x]
        value = sum + ord(char)
        sum = (value * 17) % 256

    print(sum)
    return sum


if __name__ == '__main__':
    data = read_data()
    sum = 0

    strings = data[0].split(",")
    for string in strings:
        value = get_value_for_string(string)
        sum += value

    print(sum)
