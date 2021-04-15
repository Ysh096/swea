import sys
sys.stdin = open('input.txt')

# N개 컨테이너를 M대의 트럭으로 A to B
# A도시에서 B 도시로 최대 M대의 트럭이 편도로 한번만 운행
# 이동한 화물의 총 중량이 최대가 되도록 옮기기 -> 옮겨진 화물의 전체 무게는?
# 화물을 싣지 못할 수도, 남는 화물이 있을 수도.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 화물의 무게
    weights = sorted(list(map(int, input().split())))
    # 적재 용량
    vols = sorted(list(map(int, input().split())))
    result = 0
    i = 1
    j = 1
    while M > 0 and j <= len(weights):
        if vols[-i] >= weights[-j]:
            # 이동
            result += weights[-j]
            i += 1
            j += 1
            M -= 1
        elif vols[-i] < weights[-j]:
            # 얘는 싣고 가지 못한다.
            j += 1
    print('#{} {}'.format(tc, result))
