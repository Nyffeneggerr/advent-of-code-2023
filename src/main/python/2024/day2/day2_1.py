
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def nums_valid(nums, desc):
    for i in range(0, len(nums) - 1):
        current = nums[i]
        next_num = nums[i+1]

        if current == next_num:
            return 0

        if (current < next_num) and desc:
            return 0

        if (current > next_num) and not desc:
            return 0

        if abs(current - next_num) > 3:
            return 0

        valid = True

    return 1


if __name__ == '__main__':
    data = read_data()

    valid_count = 0

    for line in data:
        nums = [int(x) for x in line.split(' ')]

        desc = nums[0] > nums[1]

        valid_count += nums_valid(nums, desc)

    print(valid_count)
