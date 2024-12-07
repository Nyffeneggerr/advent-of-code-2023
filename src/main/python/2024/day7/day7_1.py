
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def is_valid(numbers, result):
    if len(numbers) == 1:
        return numbers[0] == result

    if len(numbers) == 2:
        if numbers[0] + numbers[1] == result:
            return True

        if numbers[0] * numbers[1] == result:
            return True
    else:
        mult_result = numbers[0] * numbers[1]
        add_result = numbers[0] + numbers[1]

        mult_numbers = [mult_result] + numbers[2:]
        add_numbers = [add_result] + numbers[2:]

        return is_valid(mult_numbers, result) or is_valid(add_numbers, result)

    return False


if __name__ == '__main__':
    data = read_data()

    challenge_result = 0

    for line in data:
        result, rest = line.split(': ')
        numbers = [int(x) for x in rest.split(' ')]
        result = int(result)

        if is_valid(numbers, result):
            challenge_result += result


    print(challenge_result)
