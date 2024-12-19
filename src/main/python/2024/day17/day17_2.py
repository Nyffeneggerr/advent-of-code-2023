import math


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
        result = int(registers['B'] ^ lit_operand)
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
        result = int(registers['B'] ^ registers['C'])
        registers['B'] = result
        return ip + 2
    elif instruction == 5:
        output.append(get_combo_operand(lit_operand, registers) % 8)

        if len(output) == 1 and output[0] != program[0]:
            return 20

        if len(output) == 2 and output[:2] != program[:2]:
            return 20

        if len(output) == 3 and output[:3] != program[:3]:
            return 20

        if len(output) == 4 and output[:4] != program[:4]:
            return 20

        if len(output) == 5 and output[:5] != program[:5]:
            return 20

        if len(output) == 6 and output[:6] != program[:6]:
            return 20

        if len(output) == 7 and output[:7] != program[:7]:
            return 20

        if len(output) == 8 and output[:8] != program[:8]:
            return 20

        if len(output) >= len(program):
            return 20

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
    program = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]

    output = []
    register_a = 3556430610000000
    last_valid = 0

    while True:
        program_halted = False
        output = []
        ip = 0

        registers = {'A': register_a, 'B': 0, 'C': 0}

        while not program_halted:
            ip = move_machine(ip, program, registers, output)

            if ip >= len(program):
                program_halted = True

        if output == program:
            break

        if len(output) >= 6 and output[:6] == program[:6]:
            print("current A / diff to last: " + str(register_a) + ' / ' + str(register_a - last_valid))
            # print(str(register_a % 7))
            last_valid = register_a

        register_a += 1

    print(register_a)
