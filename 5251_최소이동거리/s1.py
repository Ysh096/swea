import sys
sys.stdin = open('input.txt')

# 0번부터 N번까지 이동하는 최소한의 거리

import heapq

def dijkstra():
    dist[0] = 0 # 0에서 0으로 가는 거리는 0
    heap = []
    # 초기 설정 가중치 0, 위치 (0, 0)
    heapq.heappush(heap, (dist[0], 0, 0))

    while heap:
        # 가장 가중치가 작은 것 부터 확인
        w, s, e = heapq.heappop(heap)
        for j in range(N+1):
            # s의 인접 정점에 대해서
            if graph[s][j]:
                # dist[j]: 0에서 j로 가는데에 드는 비용
                if dist[j] > dist[s] + graph[s][j]:
                    dist[j] = dist[s] + graph[s][j]
                    heapq.heappush(heap, (dist[j], j, e))

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    # s, e, w 가 주어짐
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    # print(graph)
    # dijkstra를 위한 초기화
    dist = [987654321]*(N+1)
    dijkstra()
    print("#{} {}".format(tc, dist[-1]))