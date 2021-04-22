import sys
sys.stdin = open('input.txt', 'r')

import heapq
def find_road():
    global result
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    heap = []
    # 시작 지점 잡기
    dist[0][0] = 0
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        # 현재 위치
        w, r, c = heapq.heappop(heap)
        if r == N-1 and c == N-1:
            return

        # 현재 위치에서 갈 수 있는 위치 확인하기
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 범위 내에 있는지 확인
            if 0 <= nr < N and 0 <= nc < N:
                # 다음 경로로 가는 데에 드는 비용
                if board[nr][nc] > board[r][c]:
                    fuel = board[nr][nc] - board[r][c] + 1
                else:
                    fuel = 1
                if dist[nr][nc] > dist[r][c] + fuel:
                    dist[nr][nc] = dist[r][c] + fuel
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))
        # 갈 수 있는 경로 다 확인했으면 그 중 가장 연료 소비가 작은 애를 확인해야 함

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 초기화
    dist = [[987654321] * N for _ in range(N)]

    find_road()
    print("#{} {}".format(tc, dist[-1][-1]))
