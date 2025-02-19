# 회문
# https://www.acmicpc.net/problem/17609

def is_palindrome(string):
    print(count_match(string, 0, len(string) - 1, 0))


def count_match(string, left, right, count):
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            if count == 0:
                # 두 가지 경우 중 최소값 반환
                return min(
                    count_match(string, left + 1, right, count + 1),
                    count_match(string, left, right - 1, count + 1)
                )
            return 2
    return count

t = int(input())
for i in range(t):
    is_palindrome(input())
