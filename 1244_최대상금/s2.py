import sys
sys.stdin = open('input.txt')

T = int(input())

def change(cnt):
    global max_val
    if cnt == k:
        val = int(''.join(nums))
        if val > max_val:
            max_val = val
        return
    for i in range(N-1):
        for j in range(i+1, N):
            nums[i], nums[j] = nums[j], nums[i]
            change(cnt+1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, T+1):
    # 두 개를 뽑아 자리를 바꾸는 모든 경우의 수를 저장
    nums, k = input().split()
    nums = list(nums)
    k = int(k)
    N = len(nums)
    max_val = 0
    if N-1 < k:
        while N-1 < k:
            k -= 2
    change(0)
    print('#{} {}'.format(tc, max_val))
