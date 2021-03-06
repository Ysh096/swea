# 단순 반복으로 풀어버림, 다른 방식으로 접근이 필요함.
import sys
sys.stdin = open('input.txt', 'r')

# # 러시아 국기를 완성하기 위해 새로 칠해야 하는 칸의 최솟값은?
# def flag_making(pos: tuple):
#     result = 0
#     W, B, R = pos[0], pos[1], pos[2]
#     # 첫째 줄을 흰색으로 바꾸기 위해 색칠할 칸 수
#     for color in flag[0]:
#         if color != 'W':
#             result += 1
#     # 마지막 칸을 빨간색으로 바꾸기 위해 색칠할 칸 수
#     for color in flag[-1]:
#         if color != 'R':
#             result += 1
#     if pos[0]: # 흰 색이 있을 경우
#         for i in range(1, 1+W):
#             for color in flag[i]:
#                 if color != 'W':
#                     result += 1
#     # 파란색의 경우 무조건 한 줄 이상
#     for i in range(1+W, 1+W+B):
#         for color in flag[i]:
#             if color != 'B':
#                 result += 1
#     if pos[2]: # 빨간 색이 있을 경우
#         for i in range(1+W+B, 1+W+B+R):
#             for color in flag[i]:
#                 if color != 'R':
#                     result += 1
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     flag = [list(input()) for _ in range(N)]
#     # N개의 줄에 M개의 문자로 이루어진 문자열이 주어진다.
#     # 일단 위에서 한 줄, 밑에서 한 줄은 각각 흰색과 빨간색이어야 하고,
#     # 중간의 색은 새로 칠해야 할 칸이 최소인 방향으로..
#     # 예시1) 중간의 색은 두 종류일 수 있고, 파란색은 무조건 한 줄 이상 들어가야 한다.
#     # 경우의 수: (W, B), (B, R), (B, B) 세 가지
#     # W, B, R의 개수의 합이 2가 되고, B는 한 개 이상 존재하는 경우의 수!
#     # 예시2) 중간에 네 줄이 있고, 흰-파-빨 순으로 배열하는 방법의 가짓수를 찾아야 한다.
#     # 경우의 수: 순서가 정해져 있으므로 개수만 정하면 될듯?
#     # W, B, R의 개수의 합이 4가 되고, B는 한 개 이상 존재하는 경우의 수!
#
#     # W, B, R의 부분집합을 구하되, 합이 N-2, B >= 1인 경우를 모두 알아야 한다.
#     possible = []
#     for B in range(1, N-2 + 1): # B의 가능한 가짓수
#         for W in range(N-2-B + 1):
#             for R in range(N-2-B + 1):
#                 if B+W+R == N-2:
#                     possible.append((W, B, R))
#     answer = []
#     for pos in possible:
#         answer.append(flag_making(pos))
#
#     min_val = answer[0]
#     for ans in answer:
#         if ans < min_val:
#             min_val = ans
#     print('#{} {}'.format(tc, min_val))


##########################################################
# 온라인 강의 풀이
# def perm(idx, sub_sum):
#     global ans
#     # 유망성 검사
#     # 아래의 조건문에 걸리게 되면 이후 작업은 의미가 없음
#     if sub_sum > N:
#         return
#
#     if idx == 3:
#         if sub_sum == N:
#             cnt = 0 # 바꿔야 하는 수
#
#             st = sel[0] # starting point
#             st2 = st + sel[1]
#
#             # 흰색 칠하기
#             for row in flag[:st]:
#                 for j in row:
#                     if j != 'W':
#                         cnt += 1
#             # 파란색 칠하기
#             for i in flag[st:st2]:
#                 for j in i:
#                     if j != 'B':
#                         cnt += 1
#             for i in flag[st2:]:
#                 for j in i:
#                     if j != 'R':
#                         cnt += 1
#             if ans > cnt:
#                 ans = cnt
#         return
#
#     # 중복순열 살짝 응용
#     for i in range(1, N-1): # 각 한줄씩은 보장해야 하므로
#         sel[idx] = i
#         perm(idx+1, sub_sum+i)
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     flag = [list(input()) for _ in range(N)]
#     sel = [0] * 3 # 세 개를 뽑을 것(W, B, R)
#     ans = 987654321
#
#     perm(0, 0)
#
#     print('#{} {}'.format(tc, ans))

##########################################################

# 행별로 W, B, R이 아닌 애들을 각각 세어보자.
# ex) 1행에서 W가 아닌 애: 2개
#     1행에서 B가 아닌 애: 5개
#     1행에서 R이 아닌 애: 3개
# 이런 식으로..
# 그리고 각 색에 대해 누적합을 구해보자.
# 각 행별-색깔별 누적합의 의미: 그 행까지 해당 색으로 칠하기 위해 바꿔야 하는 수
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    W = [0] * N
    B = [0] * N
    R = [0] * N

    # 행을 보면서 나와 다른 색깔의 개수를 카운팅
    for i in range(N):
        for j in range(N):
            if flag[i][j] != 'W':
                W[i] += 1
            if flag[i][j] != 'B':
                B[i] += 1
            if flag[i][j] != 'R':
                R[i] += 1
    # 누적 시키자.
    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]

    ans = 98754321
    # 각각의 색별로 한줄씩 이상은 확보해야 하니까
    for i in range(N-2):
        for j in range(i+1, N-1):
            w_cnt = W[i]
            b_cnt = B[j] - B[i]
            r_cnt = R[N-1] - R[j]

            if ans > w_cnt + b_cnt + r_cnt:
                ans = w_cnt + b_cnt + r_cnt
    print('#{} {}'.format(tc, ans))