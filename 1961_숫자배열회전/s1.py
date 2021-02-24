import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def ninety_degree(matrix, N, k):
    '''
    N*N matrix를 받아 k번 90도 회전시키는 함수
    '''
    rotated = [[0]*N for _ in range(N)]
    while True:
        for i in range(N):
            for j in range(N):
                rotated[j][-i-1] = matrix[i][j]
        if k != 1:
            return ninety_degree(rotated, N, k-1)
        else:
            return rotated
for tc in range(1, T+1):
    N = int(input()) #N*N행렬
    numbers = [input().split() for _ in range(N)]
    a = ninety_degree(numbers, N, 1)#90
    b = ninety_degree(numbers, N, 2)#180
    c = ninety_degree(numbers, N, 3)#270
    print('#{}'.format(tc))
    for i in range(N):
        print('{} {} {}'.format(''.join(a[i]), ''.join(b[i]), ''.join(c[i])))

