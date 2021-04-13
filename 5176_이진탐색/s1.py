import sys
sys.stdin = open('input.txt')

def in_order(node, tree):
    global cnt
    # 방문한 node가 N 이하일 때에만 값 추가
    if N >= node:
    # if node > 0:
        #left
        in_order(2*node, tree)
        tree[node] = cnt
        cnt += 1
        #right
        in_order(2*node+1, tree)

T = int(input())
# 중위 순회로 값을 하나씩 넣을 수 있지 않을까?
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1
    in_order(1, tree)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))