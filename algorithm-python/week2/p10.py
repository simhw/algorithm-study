# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

answer = 0


def solution(numbers, target):
    minus_or_plus(numbers, target, 0, 0)
    return answer


def minus_or_plus(numbers, target, sum, position):
    if position == len(numbers):
        if sum == target:
            global answer
            answer += 1
        return

    minus_or_plus(numbers, target, sum - numbers[position], position + 1)
    minus_or_plus(numbers, target, sum + numbers[position], position + 1)


numbers = [1, 1, 1, 1, 1]
target_number = 3

solution(numbers, target_number)
print(answer)
