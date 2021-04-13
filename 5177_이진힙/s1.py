import sys
sys.stdin = open('input.txt')

def heap_push(heap, item):
    global heap_cnt
    heap_cnt += 1
    heap[heap_cnt] = item
    idx = heap_cnt
    while True:
        if heap[idx] < heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx = idx//2
        else:
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0]*(N+1)
    heap_cnt = 0

    temp = list(map(int, input().split()))

    for i in range(len(temp)):
        heap_push(heap, temp[i])

    result = 0
    i = len(heap)-1
    while i > 0:
        result += heap[i//2]
        i = i//2
    print('#{} {}'.format(tc, result))