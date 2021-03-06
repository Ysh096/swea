import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    cnt = 0
    while cnt < M:
        f = q.pop(0)
        q.append(f)
        cnt += 1
    print('#{} {}'.format(tc, q[0]))