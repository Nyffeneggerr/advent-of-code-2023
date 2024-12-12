import functools

number_of_iterations = 75


@functools.cache
def get_count(blink_nr, number):
    if number == 0:
        if blink_nr == number_of_iterations - 1:
            return 1
        else:
            return get_count(blink_nr + 1, 1)
    elif len(str(number)) % 2 == 0:
        if blink_nr == number_of_iterations - 1:
            return 2
        else:
            str_value = str(number)
            center = int(len(str_value) / 2)
            return get_count(blink_nr + 1, int(str_value[:center])) + get_count(blink_nr + 1, int(str_value[center:]))
    else:
        if blink_nr == number_of_iterations - 1:
            return 1
        else:
            return get_count(blink_nr + 1, number * 2024)


if __name__ == '__main__':
    data = "27 10647 103 9 0 5524 4594227 902936"
    # data = "125 17"
    # data = "125"
    next_numbers = [int(x) for x in data.split(' ')]

    result = 0

    for i in range(len(next_numbers)):
        result += get_count(0, next_numbers[i])

    print(result)
