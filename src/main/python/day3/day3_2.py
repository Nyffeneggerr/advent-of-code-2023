import re

digit_match = "[0-9]"
gear_match = "[\*]"

def read_cards():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    part_lines = read_cards()
    total_number = 0

    for line_number, part_line in enumerate(part_lines):
        is_number_open = False
        open_number_string = ''

        for index in range(len(part_line)):
            current_char = part_line[index]
            if re.match(digit_match, current_char):
                if not is_number_open:
                    is_number_open = True

                open_number_string += current_char
            else:
                if is_number_open:
                    is_number_open = False
                    string_len = len(open_number_string)
                    is_counting_number = False
                    min_index = 0
                    max_index = string_len

                    if index - string_len - 1 > 0:
                        min_index = index - string_len - 1

                    if index < len(part_line):
                        max_index = index + 1

                    if re.search(gear_match, part_line[min_index: max_index]):
                        is_counting_number = True

                    if line_number > 0:
                        previous_line = part_lines[line_number - 1]
                        if re.search(gear_match, previous_line[min_index: max_index]):
                            is_counting_number = True

                    if line_number < len(part_lines) - 1:
                        next_line = part_lines[line_number + 1]
                        if re.search(gear_match, next_line[min_index: max_index]):
                            is_counting_number = True

                    if not is_counting_number:
                        replacement_string = ""
                        if string_len == 1:
                           replacement_string = "."
                        if string_len == 2:
                            replacement_string = ".."
                        if string_len == 3:
                            replacement_string = "..."

                        current_line = part_lines[line_number]
                        print("original     " + current_line)
                        replacement = replacement_string.join([current_line[:min_index+1], current_line[min_index+1+string_len:]])
                        print("replacement: " + replacement)
                        part_lines[line_number] = replacement

                    print(f'{open_number_string} is {is_counting_number}')

                    open_number_string = ''

    print(part_lines)
    with open('results.txt', "w") as file:
        file.write('\n'.join(part_lines))
        file.close()
