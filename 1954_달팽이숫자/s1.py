import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # matrix = [[0]*N]*N 이렇게 만들면 얕은복사여서 문제 발생
    matrix = []
    for _ in range(N):
        row_matrix = []
        for _ in range(N):
            row_matrix += [0]
        matrix += [row_matrix]
    #[]
    matrix[0][0] = 1 #초기값
    #2N-1번의 방향 전환을 한다.
    #우->하->좌->상->우->하->...
    x = 0
    y = 0
    dx = [0, 1, 0, -1]*N #방향이 담긴 배열
    dy = [1, 0, -1, 0]*N #방향이 담긴 배열
    i = 0
    val = 2
    while val <= N*N:
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=N or ny>=N or nx<0 or ny<0 or matrix[nx][ny]!=0:
            i = i+1
            continue
        else:
            matrix[nx][ny] = val
            x, y = nx, ny
            val += 1
    print('#{}'.format(tc))
    for i in range(N):
        print(*matrix[i])




