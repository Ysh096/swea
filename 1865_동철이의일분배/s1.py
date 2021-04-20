import sys
sys.stdin = open('input.txt')

# 배열 최대합..백트래킹을 어떻게 하지?
def max_p(i, result):
    global max_per
    # 소수점이므로 max_per보다 작은 것에 어떤 소수를 곱해도
    # max_per보다 커질 수 없다.
    if result <= max_per:
        return

    if i == N:
        if max_per < result:
            max_per = result
        return
    for j in range(N):
        if cols[j] == 0:
            cols[j] = 1
            max_p(i+1, result*(P[i][j])/100)
            cols[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    max_per = 0
    cols = [0]*N
    max_p(0, 1)

    print("#{} {:.6f}".format(tc, round(max_per*100, 6)))