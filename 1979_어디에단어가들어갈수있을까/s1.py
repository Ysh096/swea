import sys
sys.stdin = open('input.txt', 'r')
#받은 퍼즐의 행에서 정확히 K개만큼의 빈칸을 찾는 함수
def find_pos(puzzle, ans, K):
    for row in puzzle:
        cnt, idx = 0, 0
        while idx < len(row):
            if row[idx] == 0: #0을 만났을 때
                #만약 cnt가 K이면 K개짜리 puzzle을 맞출 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0 #그 후 초기화(처음부터 다시 세야 함)
                idx += 1
            else: #1을 만났을 때
                cnt += 1 #1이 몇 개 연속으로 붙어 있는지 세기
                idx += 1
        #0을 더이상 만나지 않고 끝까지 갔을 때
        if cnt == K:
            ans += 1
    return ans


T = int(input())
for tc in range(1, T+1): #10개의 테스트 케이스
    #N=퍼즐의 크기, K=단어의 길이
    N, K = map(int, input().split())
    puzzle = [] #퍼즐의 2차원 배열이 들어갈 공간
    for i in range(N):
        row = list(map(int, input().split()))
        puzzle += [row] #퍼즐을 2차원 배열로 받아옴
    #흰색이 1, 검은색이 0
    #행, 열 별로 1이 K번 연속인 부분 찾기!(K+1 이상은 안됨)

    ans = 0 #답을 저장할 변수
    #1. 행의 경우
    ans = find_pos(puzzle, ans, K)

    #2. 열의 경우
    #전치시키고 거기서 행의 경우를 반복해보자.
    puzzle_trans = [[0]*N for _ in range(N)] #전치행렬을 저장할 공간
    for i in range(N):
        for j in range(N):
            puzzle_trans[i][j] = puzzle[j][i]
	#전치행렬의 행(본행렬의 열)에서 빈칸 다시 찾기
    ans = find_pos(puzzle_trans, ans, K)

    print('#{} {}'.format(tc, ans))
