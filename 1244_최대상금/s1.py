import sys
sys.stdin = open('input.txt')

def selection_sort(num_list, k):
    N = len(num_list)
    cnt = 0
    while True:
        for i in range(N-1):
            max_idx = i
            for j in range(i+1, N):
                if num_list[max_idx] <= num_list[j]:
                    max_idx = j
            if num_list[max_idx] != num_list[i]: # 같은 값이 아니면 바꾸자
                num_list[max_idx], num_list[i] = num_list[i], num_list[max_idx]
                cnt += 1
            if cnt == k:
                return
        # 바꿀게 없는 경우
        while True:
            overlab = False
            for i in range(N-1):
                for j in range(i+1, N):
                    if num_list[i] == num_list[j]:
                        overlab = True
                        # 겹치는게 있으면 그냥 함수 종료
                        # (얘네끼리 바꾸면 되니까)
                        return
            else:
                num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
                cnt += 1
            if cnt >= k:
                return

T = int(input())
for tc in range(1, T+1):
    # nums: 숫자판 정보, k: 교환 횟수
    nums, k = input().split()
    num_list = list(map(int, nums))
    k = int(k)
    # 선택 정렬 하면서 counting
    selection_sort(num_list, k)
    print('#{} '.format(tc), end = '')
    for i in num_list:
        print(i, end='')
    print()
