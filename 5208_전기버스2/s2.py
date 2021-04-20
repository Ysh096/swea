import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    bus_stop = data[1:] + [0]
    possible = [0] * N

    for i in range(N):
        possible[i] = i + bus_stop[i]
    # print(possible)

    # 역순으로 했더니 좀 문제가 발생
    target = N-1
    cnt = 0
    while True:
        flag = False
        for i in range(N):
            if i == 0 and possible[i] >= target:
                flag = True
                break
            if possible[i] >= target:
                target = i
                cnt += 1
                break

        if flag:
            break
    print("#{} {}".format(tc, cnt))