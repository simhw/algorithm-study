# 최빈값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120812?language=python3

def solution(array):
    answer = 0
    counts = [0 for _ in range(1001)]

    for x in array:
        counts[x] += 1

    answer = find_max_index(counts)
    return answer


def find_max_index(array):
    max_num = 0
    max_index = 0

    for i in range(len(array)):
        if max_num == array[i]:
            max_index = -1
        elif max_num < array[i]:
            max_num = array[i]
            max_index = i

    return max_index
