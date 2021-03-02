import sys
sys.stdin = open('input.txt', 'r')

def p_or_imp(bung):
    for val in bung:
        if val < 0:
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split())) # N 명의 사람이 각각 도착하는 시간

    bung = [0]*max(arr) + [0]
    i = 0
    plus = 0
    while i < len(bung):
        if i != 0:
            if i % M == 0:
                plus += K
            bung[i] += plus
        i += 1
    for val in arr:
        for j in range(val, len(bung)):
            bung[j] -= 1

    p = p_or_imp(bung)

    print('#{} {}'.format(tc, p))



