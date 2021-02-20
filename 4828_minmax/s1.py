import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for i in range(T):
    L = int(input())
    values =list(map(int, input().split()))

    result = 0
    max_val = 0
    min_val = 10000001
    for value in values:
        if value >= max_val:
            max_val = value
    for value in values:
        if value <= min_val:
            min_val = value
    result = max_val - min_val
    print('#{} {}'.format(i+1, result))