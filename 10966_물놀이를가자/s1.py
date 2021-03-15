import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs():
    result = 0
    deq = deque(w_pos)
    while deq:
        i, j = deq.popleft()
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            # 이동한 곳이 땅이고 방문하지 않았으면
            if visited[nr][nc] < 0:
                visited[nr][nc] = visited[i][j] + 1
                result += visited[nr][nc]
                deq.append((nr, nc))
    return result
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    jido = []
    w_pos = []
    for i in range(N):
        temp = list(input())
        jido.append(temp)
        for j in range(M):
            if temp[j] == 'W':
                w_pos.append((i, j))
                visited[i][j] = 0 # 물임을 표시
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = bfs()
    print('#{} {}'.format(tc, result))
