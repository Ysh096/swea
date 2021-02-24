import sys
sys.stdin = open('input.txt', 'r')
#농장의 크기 N은 1이상 49이하의 홀수
#농작물의 가치는 0~5
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #달팽이 응용을 한번 해보자.
    #N*N 행렬 만들기
    farm = [list(map(int, list(input()))) for _ in range(N)]

    #0번째 행, N//2번째 열부터 시작해서
    #N//2번째 행, N//2번째 열에서 끝나는 대각선달팽이!
    dr = [1, 1, -1, -1]
    dc = [-1, 1, 1, -1]
    result = 0
    for row in range(N//2+1):
        r = row
        c = N//2
        i = 0
        result += farm[r][c] #초기값
        farm[r][c] = -1 #초기값 저장 후 다시 마주치지 않게
        nr = r
        nc = c
        N_limit = N-r
        while True:
            if i == 4:  # 네 방향 다 돈 경우
                break
            nr += dr[i]
            nc += dc[i]
            if 0+row<=nr<N_limit and 0+row<=nc<N_limit:
                if farm[nr][nc] != -1:
                    result += farm[nr][nc]
                    farm[nr][nc] = -1
                    r = nr
                    c = nc
                else: #-1을 만나면 방향을 바꿈
                    i += 1
            else: #범위를 벗어나는 경우
                i += 1
                nr = r
                nc = c
    print('#{} {}'.format(tc, result))
