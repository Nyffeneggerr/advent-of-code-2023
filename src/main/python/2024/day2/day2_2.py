def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def check_list(nums, desc, already_failed, is_first):
    if len(nums) <= 1:
        return 1

    if nums[0] == nums[1]:
        if already_failed:
            return 0
        else:
            already_failed = True

        if is_first:
            return check_list(nums[1:], desc, already_failed, False)
        else:
            return check_list(list_without_second_element(nums), desc, already_failed, False)

    if nums[0] < nums[1] and desc:
        if already_failed:
            return 0
        else:
            already_failed = True

        if is_first:
            return check_list(nums[1:], desc, already_failed, False)
        else:
            return check_list(list_without_second_element(nums), desc, already_failed, False)

    if nums[0] > nums[1] and not desc:
        if already_failed:
            return 0
        else:
            already_failed = True

        if is_first:
            return check_list(nums[1:], desc, already_failed, False)
        else:
            return check_list(list_without_second_element(nums), desc, already_failed, False)

    if abs(nums[0] - nums[1]) > 3:
        if already_failed:
            return 0
        else:
            already_failed = True

        if is_first:
            return check_list(nums[1:], desc, already_failed, False)
        else:
            return check_list(list_without_second_element(nums), desc, already_failed, False)

    return check_list(nums[1:], desc, already_failed, False)



def nums_valid(nums, desc):
    fault_count = 0
    i = 0

    while i < len(nums) - 1:
        current = nums[i]
        next_num = nums[i+1]

        if current == next_num:
            if fault_count == 0:
                fault_count = 1
                nums.pop(i+1)
                continue
            else:
                return 0

        if (current < next_num) and desc:
            if fault_count == 0:
                fault_count = 1
                nums.pop(i+1)
                continue
            else:
                return 0

        if (current > next_num) and not desc:
            if fault_count == 0:
                fault_count = 1
                nums.pop(i+1)
                continue
            else:
                return 0

        if abs(current - next_num) > 3:
            if fault_count == 0:
                fault_count = 1
                nums.pop(i+1)
                continue
            else:
                return 0

        i += 1

    return 1


def nums_valid2(nums, desc):
    print('checking nums: ' + str(nums))
    for i in range(0, len(nums) - 1):
        current = nums[i]
        next_num = nums[i+1]

        if current == next_num:
            return 1

        if (current < next_num) and desc:
            return 1

        if (current > next_num) and not desc:
            return 1

        if abs(current - next_num) > 3:
            return 1

    return 0


def list_without_second_element(nums):
    result = [nums[0]]
    result += nums[2:]
    return result


def is_one_comb_valid(nums, desc):
    if nums_valid2(nums, desc) == 0:
        return True

    for i in range(0, len(nums)):
        new_nums = nums.copy()
        new_nums.pop(i)
        if nums_valid2(new_nums, desc) == 0:
            return True

    return False


if __name__ == '__main__':
    data = read_data()
    # data = ["5 4 5 6 7 9 13"]

    valid_count = 0

    for line in data:
        nums = [int(x) for x in line.split(' ')]

        desc = nums[0] > nums[len(nums) - 1]

        if is_one_comb_valid(nums, desc):
            valid_count += 1

        # valid_count += nums_valid(nums, desc)
        # valid_count += check_list(nums, desc, False, True)

    print(valid_count)
