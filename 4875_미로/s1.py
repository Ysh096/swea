import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c, maze):
    # 네 방향을 살펴보고, 갈 수 있는 길을 스택에 저장하자.
    stack = [(r, c)]
    visit = []
    dr = [-1, 1, 0, 0] # 상 하 좌 우
    dc = [0, 0, -1, 1]
    while stack:
        r, c = stack.pop()
        visit.append((r, c))
        for k in range(4):
            nr = r + dr[k] # 새로운 경로를 탐색
            nc = c + dc[k]
            if 0<=nr<N and 0<=nc<N:
                if maze[nr][nc] == 3:
                    return 1
                if maze[nr][nc] == 0 and (nr, nc) not in visit:
                    stack.append((nr, nc))
                    # 네 방향을 모두 살피고, 길이 있으면 넣어줌!
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # maze = 미로의 이차원 배열 형태
    # 시작 지점을 찾자.
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
    # i, j는 미로의 시작 지점이다.
    print('#{} {}'.format(tc, dfs(r, c, maze)))

