boxes = {}


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def hash_of_label(string):
    sum = 0

    for x in range(len(string)):
        char = string[x]
        value = sum + ord(char)
        sum = (value * 17) % 256

    return sum


def parse_string(string):
    result = string.split('-')

    if len(result) == 2:
        return [result[0]]

    return string.split('=')


def get_element_of_list(elements_of_box, label):
    for index, element in enumerate(elements_of_box):
        if element[0] == label:
            return [index, element]

    return None


def add_elements_to_boxes(elements, box_number):
    label = elements[0]
    elements_of_box = boxes.get(box_number)

    if elements_of_box is None:
        elements_of_box = []

    element_in_box = get_element_of_list(elements_of_box, label)

    if len(elements) == 1 and element_in_box is not None:
        elements_of_box.remove(element_in_box[1])

    if len(elements) == 2:
        if element_in_box is None:
            elements_of_box.append(elements)
        else:
            elements_of_box[element_in_box[0]] = elements

    boxes[box_number] = elements_of_box


if __name__ == '__main__':
    data = read_data()
    sum = 0

    strings = data[0].split(",")
    for string in strings:
        elements = parse_string(string)
        box_number = hash_of_label(elements[0])
        add_elements_to_boxes(elements, box_number)

    for box_index in range(256):
        box = boxes.get(box_index)
        print(str(box_index) + ' = ' + str(box))

        if box is not None:
            for index, box_item in enumerate(box):
                sum += (box_index + 1) * (index + 1) * int(box_item[1])

    print(sum)
