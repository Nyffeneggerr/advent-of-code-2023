from thonny.plugins.micropython.api_stubs.pyb import fault_debug


def read_data():
    with open('test_data.txt') as file:
        return [line.rstrip() for line in file]


def nums_valid(nums, desc):
    fault_count = 0

    for i in range(0, len(nums) - 1):
        if len(nums) < i:
            break

        i = i - fault_count

        current = nums[i]
        next_num = nums[i+1]

        if current == next_num:
            if fault_count == 0:
                fault_count = 1
                nums.remove(next_num)
                continue
            else:
                return 0

        if (current < next_num) and desc:
            if fault_count == 0:
                fault_count = 1
                nums.remove(next_num)
                continue
            else:
                return 0

        if (current > next_num) and not desc:
            if fault_count == 0:
                fault_count = 1
                nums.remove(next_num)
                continue
            else:
                return 0

        if abs(current - next_num) > 3:
            if fault_count == 0:
                fault_count = 1
                nums.remove(next_num)
                continue
            else:
                return 0

    return 1


if __name__ == '__main__':
    data = read_data()

    valid_count = 0

    for line in data:
        nums = [int(x) for x in line.split(' ')]

        desc = nums[0] > nums[1]

        valid_count += nums_valid(nums, desc)

    print(valid_count)
