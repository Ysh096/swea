import sys
sys.stdin = open('input.txt')
# 8개의 숫자를 입력 받는다.
# 첫 번째 숫자를 1 감소한 뒤 맨 뒤로
# 다음 수는 2 감소한 뒤 맨 뒤로
# 그 다음 수는 3 감소한 뒤 맨 뒤로,
# 그 다음 수는 4 감소한 뒤 맨 뒤로
# 그 다음 수는 5 감소한 뒤 맨 뒤로
# 이게 한 사이클
# 그 다음 수 부터는 1 감소 후 뒤로 이동, 2 감소 후 뒤로 이동 , ...
# 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램이 종료됨
for _ in range(11):
    tc = int(input())
    pwd = list(map(int, input().split()))
    end = 1
    while end:
        for i in range(1, 6): #1~5까지
            val = pwd.pop(0)
            while val - i > 0:
                pwd.append(val-i)
                break
            else:
                val = 0
                end = 0
                break
    pwd.append(val)
    print('#{}'.format(tc), *pwd)

