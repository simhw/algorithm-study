# 반복되지 않는 문자
# https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/
import math
from tokenize import Number


def find_not_repeating_first_character(string):
    n = 26
    chars = [0] * n

    for i in range(n):
        ch = string[i]
        x = ord(ch) - ord('a')
        # 문자가 처음 나오는 경우
        # 문자가 등장한 위치 저장
        if chars[x] == 0:
            chars[x] = i + 1
        # 문자가 이미 나온 경우 무한대 저장
        else:
            chars[x] = math.inf

    # 최소값 찾기
    min = math.inf
    answer = ''
    for i in chars:
        x = chars[i]
        # 한번이라도 문자가 등장한 경우
        if x > 0:
            if x < min:
                min = x
                answer = chr(i + ord('a'))
            break

    print(answer)
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
