import sys
sys.stdin = open("input.txt", "r")
# def check(long, short):
#     max_value = -987654321
#     for i in range(len(long)-len(short)+1):
#         result = 0
#         for j in range(len(short)):
#             result += long[i+j]*short[j]
#         if max_value < result:
#             max_value = result
#     return max_value
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     #N, M 리스트의 길이를 의미한다. 3~20
#     N, M = map(int, input().split())
#
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     #짧은걸 움직이는게 편하다.
#
#     if N > M:
#         ans =check(A, B)
#     else:
#         ans = check(B, A)
#     print('#{} {}'.format(tc, ans))

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    result = []
    if A > B:
        for j in range(A-B+1): #0, 1, 2
            mul_plus = 0
            for i in range(B):
                mul_plus += list_B[i]*list_A[i+j]
            result += [mul_plus]
    else:
        for j in range(B-A+1):
            mul_plus = 0
            for i in range(A):
                mul_plus += list_A[i]*list_B[i+j]
            result += [mul_plus]
    max_val = result[0]
    for val in result:
        if val >= max_val:
            max_val = val
    print('#{} {}'.format(tc, max_val))