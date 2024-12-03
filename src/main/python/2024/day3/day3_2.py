import re


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


if __name__ == '__main__':
    data = read_data()
    single_line = ''.join(data) + 'do()'

    split1 = re.split('/(?=[(do\(\)|don\'t\(\))])|(?<=[(do\(\)|don\'t\(\))])/g', single_line)

    only_dos = []

    for i in range(0, len(split1)):
        print(split1[i])
        if i % 2 == 0:
            only_dos.append(split1[i])

    single_line = ''.join(only_dos)
    print(single_line)

    findings = re.findall('mul\([0-9]*,[0-9]*\)', single_line)

    number_pairs = [x[4:-1].split(',') for x in findings]

    result = 0

    for number_pair in number_pairs:
        value = int(number_pair[0]) * int(number_pair[1])
        result += value

    print(findings)
    print(number_pairs)
    print(result)

