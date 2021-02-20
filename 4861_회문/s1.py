import sys
sys.stdin = open("input.txt", "r")

# #회문은 한 개 존재!
# def Palindrome(p_list, N, M):
#     ans = []
#     for row in p_list:
#         for i in range(N-M+1):
#             cnt = 0
#             #for-else 구문을 사용하면 훨씬 간결하다...(지수님 코드)
#             if row[i] == row[i+M-1]: #처음과 끝이 같다면
#                 for j in range(M//2):
#                     if row[i+j] == row[i+M-1-j]: #그 다음도 같은지 확인
#                         cnt += 1
#                     else:
#                         break
#                     if cnt == M//2: #회문이 맞으면
#                         ans += row[i:i+M] #결과 저장
#             cnt = 0 #count 초기화
#     return ans
#
# #글자판의 크기가 N, 회문의 길이 M
# T = int(input()) #테스트 케이스
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) #N=글자판, M=회문의 길이
#     #회문의 길이가 10이라면 0과 9를 비교해보는걸 시작으로 하면 된다.
#     p_list = []
#     for i in range(N):
#         row = list(input())
#         p_list += [row]
#
#     #p_list는 글자판
#     #행의 경우
#     ans_row = Palindrome(p_list, N, M)
#
#     #열의 경우
#     #전치!
#     p_list_trans = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             p_list_trans[i][j] = p_list[j][i]
#     #함수 다시 사용
#     ans_col = Palindrome(p_list_trans, N, M)
#
#     #어떤 부분에 값이 들어있는지 확인
#     if ans_row == []:
#         ans = ans_col
#     else:
#         ans = ans_row
#     ans = ''.join(ans)
#     print('#{} {}'.format(tc, ans))




###교수님 풀이###
def my_reverse(line):
    r_line = []
    #뒤에서부터 읽어서 리스트로 만들어놓고 리턴해주자
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])
    #뒤집어진 문자열을 반환
    return r_line

def my_find():
    #전체크기가 N
    for i in range(N): #가로든 세로든 N번 검사해야함
        #가로 검사
        for j in range(N-M+1):
            #부분 문자열을 위한 빈리스트
            tmp = []
            for k in range(M):
                tmp.append(words[i][j+k]) #tmp = 원 문자열
            if tmp == my_reverse(tmp):
                return tmp #회문은 한 개가 존재하므로 바로 반환해도 된다.
        #세로 검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i]) #열 우선순회(행을 고정)
            if tmp == my_reverse(tmp):
                return tmp


T = int(input())
for tc in range(1, T+1):
    #N: 2차원 리스트의 크기 10<=N<=100
    #M: 우리가 찾고 싶은 회문의 길이 5<=M<N
    N, M = map(int, input().split())

    #리스트 내포 방식을 이용한 입력 처리
    words = [list(input()) for _ in range(N)]

    ans = my_find()

    print('#{} {}'.format(tc, ''.join(ans)))
