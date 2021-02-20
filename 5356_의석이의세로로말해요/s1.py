import sys
sys.stdin = open('input.txt')

T = int(input())
# 길이가 15이고 0으로 가득 찬 2차원 배열을 만들자
# empty list에 sen을 한 줄 한 줄 넣을 것이다.
for tc in range(1, T+1):
    empty = [[0] * 15 for _ in range(5)]
    for i in range(5):
        tmp = list(input())
        for j in range(len(tmp)):
            empty[i][j] = tmp[j]
    print('#{}'.format(tc), end=' ')
    for j in range(15):
        for i in range(5):
            if not empty[i][j] == 0:
                print(empty[i][j], end = '')
    print()



