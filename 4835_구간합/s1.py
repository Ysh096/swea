import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for i in range(1, T+1):
    L, M = map(int, input().split()) #L = length, M = 구간수
    numbers = list(map(int, input().split()))
    result = []
    for idx in range(0, len(numbers)-M+1):
        result.append(sum(numbers[idx:idx+M]))
    answer = max(result) - min(result)
    print('#{} {}'.format(i, answer))
