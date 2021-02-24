import sys
# from pandas import DataFrame as DP
sys.stdin = open('input.txt')

def Five(board):
#가로, 세로, 우하향, 좌하향
    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]
    # 행별로 만나는 모든 돌에 대해 네 가지 검사를 해볼 것이다.
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != '.':
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    cnt = 1
                    while nx > -1 and nx < N and ny > -1 and ny < N:
                        if board[ny][nx] != '.':
                            cnt += 1
                            nx = nx + dx[i]
                            ny = ny + dy[i]
                        else:
                            break
                        if cnt == 5:
                            result = 'YES'
                            return result
                    #while이 끝났는데 아직 함수 안이다?
                    #->해당 방향에는 5개짜리가 없다.
    #모든 x, y에 대해 탐색이 끝났다.
    #아직 함수를 나가지 못한 것은 5개짜리가 없다는 뜻
    result = 'NO'
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    # print(DP(board))
    print('#{} {}'.format(tc, Five(board)))



