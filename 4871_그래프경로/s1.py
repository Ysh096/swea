import sys
sys.stdin = open('input.txt')

def find_way(adj_list, S, G, visit):
    stack = [S]
    while stack:
        i = stack.pop()
        if i not in visit:
            visit.append(i) #일단 방문했으니 추가해줌
        if G in adj_list[i]:
            return 1
        else:
            for val in adj_list[i]:
                if val not in visit:
                    stack.append(val)
    return 0



T = int(input())
for tc in range(1, T+1):
    #버텍스, 엣지
    V, E = map(int, input().split())
    #인접 리스트 만들기
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        s, g = map(int, input().split())
        adj_list[s] += [g]

    #방문 표시용 리스트
    visit = []
    #출발 노드 S, 도착 노드 G
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, find_way(adj_list, S, G, visit)))