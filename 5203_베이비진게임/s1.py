import sys
sys.stdin = open('input.txt')
T = int(input())

def baby_gin(A_input, B_input, AB):
    '''
    A와 B의 데이터를 한 번 넣고 run, triplet 여부 확인
    '''
    # A의 triplet 여부
    AB[0][A_input] += 1
    if AB[0][A_input] == 3:
        return 1
    # A의 run 여부
    run = 0
    for i in range(10):
        if AB[0][i] > 0:
            run += 1
            if run == 3:
                return 1
        else:
            run = 0

    # B의 triplet 여부
    AB[1][B_input] += 1
    if AB[1][B_input] == 3:
        return 2
    # B의 run 여부
    run = 0
    for i in range(10):
        if AB[1][i] > 0:
            run += 1
            if run == 3:
                return 2
        else:
            run = 0

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    # 2차원 배열에 A, B의 데이터를 담아보자.
    AB = [[0]*10, [0]*10]
    # AB[0] = A의 데이터, AB[1] = B의 데이터
    for i in range(6):
        A_input = data[2*i]
        B_input = data[2*i+1]
        result = baby_gin(A_input, B_input, AB)
        if result: # None이 아닌 값이 나오면
            break

    if result == None:
        result = 0
    print("#{} {}".format(tc, result))
