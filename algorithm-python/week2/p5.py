# 무작위 수 찾기

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, array):
    # 정렬되어 있는 데이터일때만 이진 탐색이 가능
    array.sort()

    left = 0
    right = len(array)

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
