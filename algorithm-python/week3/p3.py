# 오름차순 삽입 정렬
input = [4, 6, 2, 9, 1]


# def insertion_sort(array):
#     n = len(array)
#     for i in range(n):
#         now = i
#         for j in range(i - 1, -1, -1):
#             if array[now] < array[j]:
#                 array[now], array[j] = array[j], array[now]
#                 now = j
#             else:
#                 break
#     return array


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            # 이전의 값이 더 크면 교환
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
            else:
                break
            j -= 1
        print("array ", array)
    return array


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ", insertion_sort([5, 8, 4, 7, 7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", insertion_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", insertion_sort([100, 56, -3, 32, 44]))
