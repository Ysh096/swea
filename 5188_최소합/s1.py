import sys
sys.stdin = open('input.txt')

# 시간초과 풀이
# # 오른쪽 이동을 1, 아래 이동을 0이라고 해보자.
# # N이 5면 1은 4번, 0도 4번 있을 수 있고, 1과 0을 4번씩 배치하는 순열과 같다.
# # 11110000 11100001 ...
# def perm(n, k):
#     global min_val
#     # 모든 원소들의 교환이 끝났다면
#     if k == n:
#         r = 0
#         c = 0
#         result = board[r][c]
#         for i in nums:
#             r = r+dr[i]
#             c = c+dc[i]
#             result += board[r][c]
#             if result > min_val:
#                 break
#         if min_val > result:
#             min_val = result
#         return
#     # 아닌 경우
#     for i in range(k, n):
#         nums[i], nums[k] = nums[k], nums[i]
#         perm(n, k+1)
#         nums[i], nums[k] = nums[k], nums[i]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     num_zeros = [0]*(N-1)
#     num_ones = [1]*(N-1)
#     nums = num_zeros + num_ones
#
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     dr = [1, 0] # 아래, 오른쪽
#     dc = [0, 1]
#     min_val = 99999999
#
#     perm(len(nums), 0)
#     print('#{} {}'.format(tc, min_val))

def move(r, c, cnt, result):
    global min_val
    if result > min_val:
        return
    if cnt == 2*N-2:
        if min_val > result:
            min_val = result
        return
    for i in range(2):
        if 0 <= r+dr[i] <= N-1 and 0 <= c+dc[i] <= N-1:
            move(r+dr[i], c+dc[i], cnt+1, result + board[r+dr[i]][c+dc[i]])
        else:
            continue

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0] # 아래, 오른쪽
    dc = [0, 1]

    # 각 위치에서 두 가지 선택이 가능
    r, c = 0, 0
    result = board[r][c]
    min_val = 99999999
    move(r, c, 0, result)
    print('#{} {}'.format(tc, min_val))
