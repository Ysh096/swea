import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 초기화
    N = int(input())

    # 문제 배점 가져오기
    nums = list(map(int, input().split()))
    L = sum(nums)
    grades = [0]*(L+1)
    grades[0] = 1
    for num in nums:
        for i in range(L, -1, -1):
            if grades[i]:
                grades[i+num] = 1

    result = grades.count(1)
    print('#{} {}'.format(tc, result))
