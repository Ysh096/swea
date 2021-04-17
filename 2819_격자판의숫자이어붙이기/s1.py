import sys
sys.stdin = open('input.txt')

def dfs(r, c, arr, cnt):
    if cnt == 6:
        result.append(arr)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, arr + board[nr][nc], cnt+1)

T = int(input())

for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j], 0)

    print('#{} {}'.format(tc, len(set(result))))