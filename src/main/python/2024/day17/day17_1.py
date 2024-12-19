import math


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def parse_data(data):
    regs = {'A': int(data[0].split(':')[1][1:]), 'B': int(data[1].split(':')[1][1:]), 'C': int(data[2].split(':')[1][1:])}
    prog = [int(x) for x in data[4].split(':')[1][1:].split(',')]

    return prog, regs


def get_combo_operand(literal_op, registers):
    if literal_op <= 3:
        return literal_op

    if literal_op == 4:
        return registers['A']
    if literal_op == 5:
        return registers['B']
    if literal_op == 6:
        return registers['C']


def move_machine(ip, program, registers, output):
    instruction = program[ip]
    lit_operand = program[ip + 1]

    if instruction == 0:
        result = int(registers['A'] / math.pow(2, get_combo_operand(lit_operand, registers)))
        registers['A'] = result
        return ip + 2
    elif instruction == 1:
        result = registers['B'] ^ lit_operand
        registers['B'] = result
        return ip + 2
    elif instruction == 2:
        result = get_combo_operand(lit_operand, registers) % 8
        registers['B'] = result
        return ip + 2
    elif instruction == 3:
        if registers['A'] == 0:
            return ip + 2
        else:
            return lit_operand
    elif instruction == 4:
        result = registers['B'] ^ registers['C']
        registers['B'] = result
        return ip + 2
    elif instruction == 5:
        output.append(str(get_combo_operand(lit_operand, registers) % 8))
        return ip + 2
    elif instruction == 6:
        result = int(registers['A'] / math.pow(2, get_combo_operand(lit_operand, registers)))
        registers['B'] = result
        return ip + 2
    elif instruction == 7:
        result = int(registers['A'] / math.pow(2, get_combo_operand(lit_operand, registers)))
        registers['C'] = result
        return ip + 2


if __name__ == '__main__':
    data = read_data()

    program, registers = parse_data(data)

    output = []
    ip = 0

    while True:
        ip = move_machine(ip, program, registers, output)

        if ip >= len(program):
            break

    print(','.join(output))
