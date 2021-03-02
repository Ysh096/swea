import sys
sys.stdin = open('input.txt')
# 원재는 연속된 N일 동안의 물건 매매가를 예측하여 알고 있다.
# 하루에 최대 1만큼 구입 가능
# 판매는 얼마든지 할 수 있다.

# ex) 3일 동안 매매가가 1, 2, 3 이라면 처음 두 날 구입 후 마지막 날에 팔면 3의 이익을 얻을 수 있다.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mae = list(map(int, input().split()))
    # 뒤에서부터 읽어서 더 큰 값이 나오기 전까지 count
    cnt = 0
    buy = 0
    result = 0
    last = mae.pop()
    while mae:
        present = mae[-1]
        if last < present:
            sell = cnt * last
            result += sell - buy
            last = mae.pop()
            cnt = 0
            buy = 0
        else: # last의 앞부분의 가격이 더 싸면 구매
            cnt += 1
            buy += mae.pop()
    sell = cnt * last
    result += sell - buy
    print('#{} {}'.format(tc, result))