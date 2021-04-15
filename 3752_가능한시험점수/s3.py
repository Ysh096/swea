import sys
sys.stdin = open('input.txt')

# 조합을 구해보자.
def comb(i, j, n, r):
    '''
    i: c에 숫자를 넣을 위치
    j: grades에서 뽑기 시작할 위치
    n: 전체 길이
    r: 뽑는 횟수
    '''
    if i == r:

        return
    else:
        for k in range(j, n-r+i+1):
            c[i] = grades[k]
            comb(i+1, k+1, n, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grades = list(map(int, input().split()))
    # nCr에서 r이 변함
    for r in range(1, N):
        c = [0]*r
        comb(0, 0, len(grades), r)