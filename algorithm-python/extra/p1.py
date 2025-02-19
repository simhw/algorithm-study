# 주몽
# https://www.acmicpc.net/problem/1940

# 투 포인터
# 정렬된 리스트에서 특정 합이 되는 요소 쌍을 찾는 문제
def is_pair_sum(nums, target):
    answer = 0
    left = 0
    right = len(nums) - 1

    nums.sort()

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            answer += 1
            left += 1
            right -= 1
        elif sum < target:
            left += 1
        else:
            right -= 1

    print(answer)


n = int(input())
m = int(input())
nums = list(map(int, input().split()))

is_pair_sum(nums, m)
