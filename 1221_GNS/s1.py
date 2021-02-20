import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    tc, _ = input().split()
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    nums_cnt = [0] * 10 #counting list
    num_list = input().split()
    for val in num_list:
        for idx, num in enumerate(nums):
            if val == num:
                nums_cnt[idx] += 1 #인풋을 읽어가며 숫자 세기
                break
    print(tc)
    for i in range(10):
        print(('{} '.format(nums[i]))*nums_cnt[i], end = '')