import sys
sys.stdin = open("input.txt", "r")

T = int(input())
nums = list(range(1, 13))
n = len(nums)
for tc in range(1, T+1):
    cnt = 0
    N, K = map(int, input().split())
    for i in range(1<<n):
        result = []
        for j in range(n):
            if i & (1<<j):
                result += [nums[j]]

        result_sum = 0
        for val in result:
            result_sum += val

        if len(result) == N and result_sum == K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
