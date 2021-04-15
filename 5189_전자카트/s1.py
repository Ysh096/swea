import sys
sys.stdin = open('input.txt')

# 한 번씩만 방문, 최소 배터리 사용량은?
def perm(k, n): # k: 바꿀 위치, n: 리스트 길이
    global min_val
    # 1에서 시작해서 1로 돌아온다.
    # ex) N=3이면 2와 3의 순열만 만들면 됨
    if k == n:
        result = data[0][roads[0]]
        for i in range(1, N-1):
            result += data[roads[i-1]][roads[i]] # i-1 인덱스에서 i 인덱스로 이동
        result += data[roads[-1]][0]
        if result < min_val:
            min_val = result
        return
    else:
        for i in range(k, n):
            roads[i], roads[k] = roads[k], roads[i]
            perm(k+1, n)
            roads[i], roads[k] = roads[k], roads[i]

T = int(input())
for tc in range(1, T+1):
    # 3 <= N <= 10
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 0부터 N-1까지의 순열 + 0으로 돌아가기
    roads = [i for i in range(1, N)]
    # roads의 순열을 구한다.
    min_val = 999999999
    perm(0, N-1)
    print('#{} {}'.format(tc, min_val))