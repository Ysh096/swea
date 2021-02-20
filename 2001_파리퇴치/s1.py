import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 파리가 들어있는 배열 만들기
    fly = []
    for _ in range(N):
        fly += [list(map(int, input().split()))]

    result = []
    for row_start in range(0, N-M+1):
        for col_start in range(0, N-M+1):
            pre_result = 0
            for i in range(M):
                for j in range(M):
                    pre_result += fly[row_start + i][col_start+j]
            result += [pre_result]
    max_val = 0
    for val in result:
        if val >= max_val:
            max_val = val
    print('#{} {}'.format(tc, max_val))