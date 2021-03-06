import sys
sys.stdin = open("input.txt", "r")

# V 개의 노드, E 개의 방향성 없는 간선 정보가 있다.
# 출발 노드에서 몇 개의 간선을 지나면 도착 노드에 갈 수 있는가?
def bfs(que, nod_list, visit):
    while que:
        road = que.pop(0) # 현재 위치
        for i in nod_list[road]:
            if visit[i] == -1:
                que.append(i)
                visit[i] = visit[road] + 1 # 다음에 갈 위치
                if i == G:
                    return visit[i]
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 연결 리스트 만들기
    nod_list = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split()) # 간선 정보
        nod_list[a].append(b)
        nod_list[b].append(a)
    S, G = map(int, input().split())
    que = [S]
    visit = [-1] * (V+1)
    visit[S] = 0
    print('#{} {}'.format(tc, bfs(que, nod_list, visit)))
