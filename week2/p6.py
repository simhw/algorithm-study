# 팩토리얼
# https://www.acmicpc.net/problem/10872

# factorial(n) = n * factorial(n - 1)
# factorial(n - 1) = (n - 1) * factorial(n - 2)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


n = int(input())
print(factorial(n))
