import sys
sys.stdin = open("input.txt", "r")

#0 -> N 정류장까지
# 한 번 충전으로 이동할 수 있는 정류장 수 K
# 충전기는 M개의 정류장에 설치
# 첫 줄에 노선 수 T(반복 횟수)
# 둘째줄 각 노선별 K, N(정류장 번호), M(충전기 설치된 정류장 수)
# 셋째줄 충전기 설치된 정류장 번호
# 거꾸로 가는게 좋지 않을까? (정류장이 주어져있어서 안됨)
def answer(K, N, M, M_list):
    for i in range(len(M_list)-1):
        if M_list[i]-M_list[i-1] > K:
            return 0
    else:
        step = 0
        count = 0
        while True:
            step += K
            if step >= N:
                break
            else:
                pre_oilbank = [i for i in M_list if i <= step]
                step = pre_oilbank[-1]
                count += 1
        return count

    #0->3까지 가보고 M_list에서 3에 가장 가까운 충전소(3보다 작거나 같은)에서 충전
T = int(input())
for i in range(1, T+1):
    L = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    K = L[0]
    N = L[1]
    M = L[2]
    result = answer(K, N, M, M_list)
    print('#{} {}'.format(i, result))





