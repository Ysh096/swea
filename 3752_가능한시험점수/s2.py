import sys
sys.stdin = open('input.txt')

T = int(input())
# 제한시간 초과 풀이2 (더 오래 걸림)
for tc in range(1, T+1):
    N = int(input())
    # 1 이상 100 이하의 자연수 모음
    grades = list(map(int, input().split()))
    # on-off 형식으로 풀어보자.
    # 시험 문제의 수가 N 이고, 각각의 경우 맞추거나 틀리거나의 2가지 경우가 있다.
    # 맞추면 1, 틀리면 0이라고 해보자.
    result = set()
    for i in range(2**N):
        temp = 0
        for j in range(N):
            if i & (1<<j):
                temp += grades[j]
        result.add(temp)
    # print(grade_dict)
    print("#{} {}".format(tc, len(result)))