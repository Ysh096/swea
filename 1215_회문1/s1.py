import sys
sys.stdin = open("input.txt", "r")

def transpose(matrix, length = 8):
    matrix_trans = []
    for j in range(length):
        tmp = ''
        for i in range(length):
            tmp += matrix[i][j]
        matrix_trans.append(tmp)
    return matrix_trans

def counting(matrix, length, N, result = 0):
    for i in range(length):
        matrix[i] = '0' + matrix[i] + '0' #양옆에 패딩

    for row in matrix:
        for i in range(length-N + 1):
            if row[i+1:i+1+N] == row[i+N:i:-1]:
                result += 1
    return result


for tc in range(1, 11):
    N = int(input()) #회문의 길이
    length = 8 #8*8글자판
    # 글자판 완성
    guelja = []
    result = 0 #결과를 저장할 변수
    for _ in range(8):
        guelja.append(input())
    guelja_trans = transpose(guelja)
    result = counting(guelja, length, N)
    result = counting(guelja_trans, length, N, result)

    print('#{} {}'.format(tc, result))


