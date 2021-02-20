import sys
sys.stdin = open('input.txt', 'r')

#bubble sort
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(N-1): #N-1번 반복
        for j in range(N-1-i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    print('#{}'.format(tc), *num_list)

#선택정렬
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(len(num_list)):
        min_num = num_list[i]
        for j in range(i+1, len(num_list)):
            if min_num > num_list[j]:
                min_num = num_list[j]
                j_idx = j
        if min_num != num_list[i]:
            num_list[i], num_list[j_idx] = num_list[j_idx], num_list[i]

    print('#{}'.format(tc), *num_list)
