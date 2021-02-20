import sys
sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     bus_stop = [0] * 5001
#
#     for i in range(N):
#         A, B = map(int, input().split())
#
#         for j in range(A, B+1):
#             bus_stop[j] += 1
#     P = int(input()) #우리가 확인하고 싶은 버스정류장의 수
#
#     print('#{}'.format(tc), end=" ")
#     for i in range(P):
#         C = int(input())
#         print(bus_stop[C], end=" ")

#첫 번째 줄 테스트 케이스 개수 T
#두 번째 줄 버스 노선 개수 N
#그 다음 N번째 줄에는 A_i, B_i값
#그 다음 줄에는 P개의 버스 정류장을 읽을 것이라는 정보
#그 다음 P개 줄에는 알고싶은 정류장 번호

#A_i, B_i는 해당 버스 노선이 A_i이상, B_i이하인 버스 정류장만을 지난다는 의미
T = int(input())

for tc in range(1, T+1):
    bus_stop = [0] * 5001
    N = int(input())
    for _ in range(N):
        AB = input().split()
        A = int(AB[0])
        B = int(AB[-1])
        for idx in range(A, B+1):
            bus_stop[idx] += 1

    P = int(input())
    print('#{} '.format(tc), end='')
    for _ in range(P):
        i = int(input())
        print('{}'.format(bus_stop[i]), end=' ')
    print()



