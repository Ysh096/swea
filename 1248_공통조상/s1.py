import sys
sys.stdin = open('input.txt')

def pre_order(node):
    global cnt
    if node > 0:
        # print(node, end=' ')
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])
    return
T = int(input())
for tc in range(1, T+1):
    # 정점의 수, 간선의 수, 공통 조상을 찾는 두 개의 정점 번호
    V, E, n1, n2 = map(int, input().split())
    # 부모-자식 순서의 간선 E개
    edges = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    for i in range(E):
        # 자식노드 넣기
        if tree[edges[2*i]][0]:
            tree[edges[2*i]][1] = edges[2*i+1]
        else:
            tree[edges[2*i]][0] = edges[2*i+1]
        # 부모노드 넣기
        if not tree[edges[2*i+1]][2]:
            tree[edges[2*i+1]][2] = edges[2*i]
    # print(tree)
    # n1과 n2의 공통 조상은 tree에서 n1, n2를 거슬러 올라가다 같은 값이 나오면 그 값!
    v_result = 0
    flag = 0
    while v_result == 0:
        # n1 != n2 이므로 무조건 한 번씩은 부모 노드를 확인해 봐야 한다.
        n1 = tree[n1][2]
        n2_node = tree[n2][2]
        # 그 후 n1에 대해 조상을 끝까지 거슬러 올라가는 n2_node를 비교해본다.
        while n2_node > 0:
            n2_node = tree[n2_node][2]
            if n1 == n2_node:
                v_result = n1
                flag = 1
                break
        if flag:
            break



    # 전위 순회
    cnt = 0
    # pre_order(v_result)
    pre_order(v_result)
    print('#{} {} {}'.format(tc, v_result, cnt))