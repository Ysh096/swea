import sys
sys.stdin = open("input.txt", "r")

def bfs(Map, que, visit):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    while que:
        r, c = que.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if Map[nr][nc] == 3:
                    return visit[r][c]
                if Map[nr][nc] == 0 and visit[nr][nc] < 0:
                    que.append((nr, nc))
                    visit[nr][nc] = visit[r][c] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]

    # 출발 지점 찾기
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                break
        if Map[i][j] == 2:
            break
    # i, j가 출발 지점
    que = [(i, j)]
    visit = [[-1] * N for _ in range(N)]
    visit[i][j] = 0
    print('#{} {}'.format(tc, bfs(Map, que, visit)))
