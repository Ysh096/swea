import sys
sys.stdin = open('input.txt', 'r')
#9*9 스도쿠 퍼즐의 검증
T = int(input())
#sort를 오랜만에 써보자.
def check_two_case(three_row: list): #세 줄씩 입력이 들어오면
    one_to_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s_1, s_2, s_3 = [], [], []
    for row in three_row: #한 줄을 검사할 때
        s_1.extend(row[0:3]) #세 개씩 끊어서 새로운 리스트에 넣어주고
        s_2.extend(row[3:6])
        s_3.extend(row[6:9])
        if sorted(row) != one_to_nine: #한 줄이 조건을 만족하는지 확인
            return False #이걸 세 번 반복하면 s1, s2, s3에 각각 3*3 숫자가 들어감
    if sorted(s_1) != one_to_nine: return False #3*3 배열이 조건을 만족하는지 각각 확인
    if sorted(s_2) != one_to_nine: return False
    if sorted(s_3) != one_to_nine: return False
    return True
def last_case(matrix: list):
    one_to_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    transpose = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            transpose[j][i] = matrix[i][j]
    for row in transpose:
        if sorted(row) != one_to_nine:
            return False
    return True
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # 1. 각 line별 체크 + 3*3 케이스
    result = []
    result.append(check_two_case(puzzle[0:3]))
    result.append(check_two_case(puzzle[3:6]))
    result.append(check_two_case(puzzle[6:9]))
    result.append(last_case(puzzle))
    if False in result:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 1))