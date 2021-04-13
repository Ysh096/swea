import sys
sys.stdin = open('input.txt')

T = int(input())
# 배열의 세로 N, 가로 M
numbers = {'0001101': 0,
           '0011001': 1,
           '0010011': 2,
           '0111101': 3,
           '0100011': 4,
           '0110001': 5,
           '0101111': 6,
           '0111011': 7,
           '0110111': 8,
           '0001011': 9, }
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    # print(data)
    # 총 56개의 숫자로 정보를 파악한다.
    # 숫자의 뒤는 모두 1로 끝나므로, 뒤부터 56개를 읽으면 된다.
    flag = False
    for i in range(N):
        for j in range(M-1, -1, -1):
            if data[i][j] == '1':
                code = data[i][j-55:j+1]
                flag = True
                break
        if flag:
            break
    # code의 앞에서부터 7개씩 읽어가며 검증해보자.
    odds = []
    evens = []
    for i in range(8):
        k = 7*i
        num = code[k:k + 7]
        # 홀수번째, 짝수번째에 따라 연산 구분
        if (i+1) % 2: # i가 홀수면(0이 아니라 1부터 시작해서 그냥 이렇게 함)
            odds.append(numbers[num])
        else:
            evens.append(numbers[num])
    if (sum(odds)*3 + sum(evens)) % 10:
        output = 0
    else:
        output = sum(odds) + sum(evens)
    print('#{} {}'.format(tc, output))



