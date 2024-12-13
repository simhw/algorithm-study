# 최대값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120812?language=python3

# input
numbers = [int(input()) for x in range(9)]

def find_max_num(array):
    max_num = 0
    max_index = 0

    for i in range(len(array)):
        if max_num < array[i]:
            max_num = array[i]
            max_index = i

    print(max_num)
    print(max_index + 1)

find_max_num(numbers)
