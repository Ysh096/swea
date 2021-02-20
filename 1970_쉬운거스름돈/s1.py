import sys
sys.stdin = open("input.txt", "r")
T = int(input())
changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    N = input()
    if N[-1] != '0':
        N = N[:-1] + '0'
    N = int(N)

    result = []
    for change in changes:
        result = result + [N // change]
        N -= change * (N // change)
    print('#{}\n {}'.format(tc, ' '.join(map(str, result))))
