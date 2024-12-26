# 회문
# https://www.acmicpc.net/problem/17609

# 런타임 에러 (RecursionError)

def is_palindrome(string):
    count_match(string, 0, len(string) - 1, 0)
    print(answer)


def count_match(string, left, right, count):
    if left > right:
        global answer
        answer = min(answer, count)
        return

    if string[left] == string[right]:
        count_match(string, left + 1, right - 1, count)
    else:
        if count == 0:
            count_match(string, left + 1, right, count + 1)
            count_match(string, left, right - 1, count + 1)
        return


t = int(input())
for i in range(t):
    answer = 2
    is_palindrome(input())
