import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = [[0]*10 for _ in range(10)] #10*10격자
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split()) #좌표와 색 받아오기
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if not result[i][j]:
                    result[i][j] = color #좌표에 색칠하기
                elif result[i][j] == color: #같은 색일 때
                    pass
                else:
                    result[i][j] += color

    cnt = 0 #칸 수를 세는 변수
    for row in result:
        for val in row: #각 원소에 대해
            if val >= 3: #딱 3일 때 말고 3보다 크거나 같을 때
                cnt += 1
    print('#{} {}'.format(tc, cnt))
