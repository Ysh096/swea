import sys
sys.stdin = open('input.txt')

def solution(H, i):
    '''
    H: 점원의 키의 합
    '''
    global min_h
    if H > min_h:
        return
    if H >= B and min_h > H: # 탑의 높이가 B이상이고 H가 min_h보다 작으면
        min_h = H
        return
    if i >= N:
        return
    solution(H+heights[i], i+1)
    solution(H, i+1)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    min_h = 99999999999
    solution(0, 0)
    print("#{} {}".format(tc, min_h-B))