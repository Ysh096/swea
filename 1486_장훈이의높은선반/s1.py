import sys
sys.stdin = open('input.txt')

# 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑 찾기
# 틀린 풀이(높이만 가장 낮으면 되는데..)
T = int(input())
for tc in range(1, T+1):
    # N은 사람의 수, B는 높이
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    heights.sort()
    result = 0
    flag = False
    for i in range(N-1, -1, -1):
        result += heights[i]
        if result >= B:
            temp = result
            result -= heights[i]
            flag = True # 찾음
            continue
        elif flag:
            break
    print('#{} {}'.format(tc, temp-B))


