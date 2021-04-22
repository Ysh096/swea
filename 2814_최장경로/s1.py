import sys
sys.stdin = open('input.txt')

def dfs(i, cnt):
    global max_cnt
    visited[i] = 1
    for j in range(1, N+1):
        if graph[i][j] and not visited[j]:
            dfs(j, cnt+1)
            visited[j] = 0
        if cnt > max_cnt:
            max_cnt = cnt

T = int(input())

for tc in range(1, T+1):
    # N 정점, M 간선
    N, M = map(int, input().split())

    graph = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    # 무방향 그래프
    # 두 정점 사이에 여러 개의 간선이 존재할 수 있다.
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    # 역시 크기가 크지 않으므로..반복문 사용
    max_cnt = 0
    for i in range(1, N+1):
        dfs(i, 1)
        visited = [0]*(N+1)

    print("#{} {}".format(tc, max_cnt))