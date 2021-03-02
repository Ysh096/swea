import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    fly = (D/(A+B))*F
    print('#{} {}'.format(tc, fly))