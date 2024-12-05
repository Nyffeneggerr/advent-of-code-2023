import functools

rules = {}

def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def is_invalid(page_list, rules):
    for i in range(len(page_list)):
        pages_before = page_list[:i]
        pages_after = page_list[i+1:]
        page = page_list[i]

        page_rule = rules[page]

        for page_before in pages_before:
            if page_before in page_rule['after']:
                return True

        for page_after in pages_after:
            if page_after in page_rule['before']:
                return True

    return False

def compare(x, y):
    pages_after = rules[x]['after']
    pages_before = rules[x]['before']

    if y in pages_after:
        return 1

    if y in pages_before:
        return -1

    return 1


def sort_get_middle(page_list, rules):
    print(page_list)
    sorted_pages = sorted(page_list, key=functools.cmp_to_key(compare))
    print(sorted_pages)

    return sorted_pages[int(len(sorted_pages)/2)]


if __name__ == '__main__':
    data = read_data()

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
        if is_invalid(page_list, rules):
            total += sort_get_middle(page_list, rules)


    print(total)


    # print(rules)
    # print(pages)
