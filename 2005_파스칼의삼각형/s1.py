import sys
sys.stdin = open('input.txt', 'r')
# 1. for문으로 풀기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p_list = [[1]*(i+1) for i in range(N)]

    for i in range(N):
        if i > 1:
            for j in range(len(p_list[i])):
                if j > 0 and j < len(p_list[i])-1:
                    p_list[i][j] = p_list[i-1][j-1] + p_list[i-1][j]
    print('#{}'.format(tc))
    for i in range(N):
        print(*p_list[i])

# 2. 조합 재귀함수 이용하기
#이걸 어떻게 스택으로 풀지??
#파스칼의 삼각형에서 발견할 수 있는 이항정리의 각 항의 성질!
#nCk = n-1_C_k-1 + n-1_C_k
#이를 바탕으로 조합의 combination을 구성하면?
def combination(n, k):
    arr[n][k] += 1
    if k == 0 or k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (i+1) for i in range(N)]
    print('#{}'.format(tc))
    for n in range(N):
        for k in range(n+1):
            print(combination(n, k), end = ' ')
        print()
#     print(arr)
# N = 6일 때, arr = [[1], [16, 16], [8, 15, 8], [4, 7, 7, 4], [2, 3, 3, 3, 2], [1, 1, 1, 1, 1, 1]]


# 3. 스택?인지는 모르겠고 여기서 두 번 검사할 필요 없게 만드는 방법
#N이 매우 커질 때 그냥 재귀와는 비교할 수 없을만큼 빠르다! for문이랑 속도가 비슷함.
def combination(n, k):
    # arr[n][k] += 1
    if k == 0 or k == n:
        comb[n][k] = 1
    elif comb[n][k] == -1:
        comb[n][k] = comb[n-1][k-1] + comb[n-1][k]
    return comb[n][k]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # arr = [[0] * (i + 1) for i in range(N)] #몇 번 호출되는지 파악해보자.
    comb = [[-1]*(i+1) for i in range(N)]
    print('#{}'.format(tc))
    for n in range(N):
        for k in range(n+1):
            print(combination(n, k), end = ' ')
        print()
    # print(arr)
# N=6일 때, arr = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]