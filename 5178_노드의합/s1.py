import sys
sys.stdin = open('input.txt')

def post_order(n):
    if n > N:
        return
    post_order(2*n)
    post_order(2*n+1)
    nodes[n//2] += nodes[n]

# 완전 이진 트리
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    nodes = [0]*(N+1)
    for i in range(M):
        leaf_node, num = map(int, input().split())
        nodes[leaf_node] = num
        end = len(nodes)
    # print(nodes)
    post_order(1)
    print('#{} {}'.format(tc, nodes[L]))
