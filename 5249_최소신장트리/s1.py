import sys
sys.stdin = open('input.txt')

def make_set(n):
    return list(range(n+1))

def find_set(x):
    if p[x] != x:
         p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
# 마지막 노드번호 V, 간선의 개수 E
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append((n1, n2, w))
    graph.sort(key=lambda x: x[2]) # 가중치 순으로 정렬

    # 최소 신장 트리
    p = make_set(V)
    result = 0
    cnt = 0 # 개수 세기
    while cnt < V:
        for data in graph:
            u, v, w = data[0], data[1], data[2]
            if find_set(u) != find_set(v):
                union(u, v)
                result += w # 가중치 합
                cnt += 1
    print("#{} {}".format(tc, result))




