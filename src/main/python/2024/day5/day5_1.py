
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def is_valid(page_list, rules):
    for i in range(len(page_list)):
        pages_before = page_list[:i]
        pages_after = page_list[i+1:]
        page = page_list[i]

        page_rule = rules[page]

        for page_before in pages_before:
            if page_before in page_rule['after']:
                return 0

        for page_after in pages_after:
            if page_after in page_rule['before']:
                return 0

    return page_list[int(len(page_list)/2)]



if __name__ == '__main__':
    data = read_data()

    rules = {}
    pages = []

    for line in data:
        if '|' in line:
            reference, after_page = [int(x) for x in line.split('|')]

            if reference in rules:
                rules[reference]['after'].append(after_page)
            else:
                rules[reference] = {
                    'before': [],
                    'after': [after_page]
                }

            if after_page in rules:
                rules[after_page]['before'].append(reference)
            else:
                rules[after_page] = {
                    'before': [reference],
                    'after': []
                }

        if ',' in line:
            pages.append([int(x) for x in line.split(',')])

    total = 0

    for page_list in pages:
        total += is_valid(page_list, rules)


    print(total)


    # print(rules)
    # print(pages)
