# 이진 탐색
from itertools import count

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 이진 탐색
def is_existing_target_number_binary(target, array):
    left = 0
    right = len(array) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1

        if array[mid] == target:
            print(count)
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 순차 탐색
def is_existing_target_number_sequential(target, array):
    count = 0
    for number in array:
        count += 1
        if target == number:
            print(count)
            return True

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
