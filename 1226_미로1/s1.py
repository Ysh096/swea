import sys
sys.stdin = open('input.txt')
# from pandas import DataFrame
# 1은 벽, 0은 길, 2는 출발점, 3은 도착점
# bfs로 풀어보자.
def bfs(miro, que, visit):
    dr = [-1, 1, 0, 0] # 상하좌우
    dc = [0, 0, -1, 1]
    while que:
        i, j = que.pop(0)
        visit[i][j] = 1
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if miro[nr][nc] == 3: # 종료 지점이다
                return 1
            elif miro[nr][nc] == 0 and visit[nr][nc] != 1: # 방문하지 않은 길이 있다.
                que.append((nr, nc))
    return 0


for _ in range(10):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    # 길이 있으면 que에 추가해주는 방식
    # 시작 지점 찾기
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                break
        if miro[i][j] == 2:
            break
    # i, j가 출발 지점
    que = [(i, j)]
    visit = [[0]*16 for _ in range(16)]
    print('#{} {}'.format(tc, bfs(miro, que, visit)))