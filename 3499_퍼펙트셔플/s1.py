#카드 덱을 정확히 반으로 나누고
#나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만든다.
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_list = input().split()
    if N % 2: #홀수면
        half = N//2 + 1
    else:
        half = N//2
    first = card_list[:half]
    second = card_list[half:]
    result = []
    while True:
        i = 0
        while i < len(first):
            result.append(first[i])
            try:
                result.append(second[i])
                i += 1
            except:
                i += 1
        break
    print('#{}'.format(tc), *result)