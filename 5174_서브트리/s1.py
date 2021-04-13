import sys
sys.stdin = open('input.txt')

# 부모와 자식 노드 번호 사이에 특별한 규칙이 없음.
# 부모가 없는 노드는 전체의 루트 노드
def pre_order(n):
    global cnt
    if n > 0:
        cnt += 1
        pre_order(tree[n][0])
        pre_order(tree[n][1])
T = int(input())
for tc in range(1, T+1):
    # N = 서브 트리의 루트, E = 간선의 수
    E, N = map(int, input().split())
    V = E + 1

    # 트리 만들기
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    edges = list(map(int, input().split()))
    for i in range(E):
        if tree[edges[2*i]][0]:
            tree[edges[2*i]][1] = edges[2*i+1]
        else:
            tree[edges[2*i]][0] = edges[2*i+1]
        tree[edges[2*i+1]][2] = edges[2*i]
    # 서브트리에 속한 노드의 개수 찾기
    # 왼쪽과 오른쪽 자식을 0이 될 때까지 찾아가면 됨
    cnt = 0
    pre_order(N)
    print('#{} {}'.format(tc, cnt))