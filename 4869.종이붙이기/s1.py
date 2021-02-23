#종이붙이기
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def find_method(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return find_method(N-20)*2 + find_method(N-10)
for tc in range(1, T+1):
    N = int(input())
    ans = find_method(N)
    print('#{} {}'.format(tc, ans))