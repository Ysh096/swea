import sys
sys.stdin = open('input.txt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    L = int(input())
    num_list = [int(val) for val in input().split()]
    #선택정렬
    for i in range(L):
        min = num_list[i]
        for j in range(i, L):
            if min > num_list[j]:
                min = num_list[j] #최솟값 찾기
                idx = j
        if min != num_list[i]:
            num_list[i], num_list[idx] = num_list[idx], num_list[i]

    #번갈아가며 나오는 새로운 리스트를 만들자
    pre_result = []
    result = []
    # 아래처럼 읽어 나갈 것이다.
    # 1 2 3 4 5 6 7 8 9 10
    # --->            <---
    if L % 2 == 0: #짝수 개 일때
        for i in range(int(L/2)):
            pre_result = [num_list[-i-1]] + pre_result + [num_list[i]] #2개씩 끊어서 저장
            result += pre_result #최종 결과를 저장
            pre_result = [] #초기화
    else: #홀수 개 일때
        for i in range(int(L/2)): #0 1 2 3
            pre_result = [num_list[-i - 1]] + pre_result + [num_list[i]]  # 2개씩 끊어서 저장
            result += pre_result  # 최종 결과를 저장
            pre_result = []  # 초기화
        result += [num_list[i+1]]
    print('#{}'.format(tc), *result[:10])


s_list = [[1, 2, 3], [4, 5, 6]]
print(s_list[0][1:5])
