import sys
sys.stdin = open('input.txt')

def dfs(r, c, cnt, val):
    global max_val
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if rooms[nr][nc] == rooms[r][c] + 1:
                dfs(nr, nc, cnt+1, val)
    if max_val <= cnt:
        max_val = cnt
        result.append((val, cnt+1))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = []
    max_val = 0
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, rooms[i][j])

    result.sort(key=lambda x: (-x[1], x[0]))
    print('#{}'.format(tc), *result[0])
