import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    # 앞 시간으로 정렬
    times.sort(reverse=True)
    result = 1
    comp = times[0]
    for i in range(1, N):
        if comp[0] >= times[i][1]:
            result += 1
            comp = times[i]
    print('#{} {}'.format(tc, result))