import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    fc = B[0] #B의 첫 번째 글자
    cnt = 0
    a, b = len(A), len(B)
    i = 0
    while i < a:
        if fc == A[i]:
            if B == A[i:i+b]:
                cnt += 1
                i += b
            else:
                i += 1
        else: i += 1
    ans = cnt + a-(b*cnt)
    print('#{} {}'.format(tc, ans))

