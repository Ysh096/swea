import sys
sys.stdin = open('input.txt')
# 화학 물질이 담긴 용기들이 사각형을 이룸
# 사각형 내부에는 빈 용기가 없음
# 두 개의 사각형 사이에는 빈 용기가 있음
# 큰 힌트! 사각형의 각 행의 수와 열의 수는 서로 다르다.
def find_info(matrix):
    i, j = 1, 1
    start = [] # 시작 지점을 저장할 리스트
    end = []
    while i < n+1:
        while j < n+1:
            if matrix[i][j] != 0 and matrix[i][j-1] == 0:
                start.append((i, j))
            elif matrix[i][j] == 0 and matrix[i][j-1] != 0:
                end.append((i, j-1))
            elif matrix[i][j] == 0:
                pass
            j += 1
        i += 1
        j = 1
    for i in range(len(start)):
        length = end[i][1] - start[i][1] + 1
        row_length[length] += 1

    return row_length

T = int(input()) # 테스트 케이스의 수
for tc in range(1, T+1):
    n = int(input())
    # 2차원 패딩이 들어간 배열로 받기
    matrix = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    matrix = [[0]*(n+2)] + matrix + [[0]*(n+2)]
    row_length = [0]*(n+1) # row_length가 같은 것의 수를 세자.
    # print(matrix)
    result = find_info(matrix)

    # 부분 행렬의 개수, 각 행렬의 행과 열의 길이를 출력
    # 출력은 행*열이 작은 순서로!
    # ex) 3 / 2 3 / 3 4 / 4 5
    # result 의 value가 행, 인덱스가 열의 길이이다.
    # 행, 열 순으로 나열해보자.
    answer = []
    for idx, val in enumerate(result):
        if val != 0:
            answer.append([val, idx])
    # 우선 행 순서로 정렬을 해줘야 함
    # answer = sorted(answer, key = lambda x: x[0])

    # 1. 부분 행렬의 개수 a
    a = len(answer)
    # 2. 크기 순으로 정렬하기
    for i in range(len(answer)):
        size = answer[i][0] * answer[i][1]
        answer[i].append(size)

    # ans = sorted(answer, key = lambda x: x[2]) # 크기를 기준으로 정렬
    answer.sort(key=lambda x: (x[0] * x[1], x[0]))
    ans_for_print = []
    for val in answer:
        ans_for_print.append(val[0])
        ans_for_print.append(val[1])
    # 3. 출력하기
    print('#{} {}'.format(tc, a), *ans_for_print)
