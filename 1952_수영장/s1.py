import sys
sys.stdin = open('input.txt')
T = int(input())
# 완전탐색
# 이용권을 조합하는 모든 상황을 만들어야한다.
# 다 더해서 12를 넘는 경우의 수를 따져보자.
def dfs(f_choices, n, cost):
    global min_cost
    if n >= 12:
        result.append(cost)
        if min_cost > cost:
            min_cost = cost
        return cost
    for choice in f_choices:
        if cost > min_cost:
            return
        if choice == 'd':
            cost += d * plan[n]
            n += 1
            dfs(f_choices, n, cost)
            n -= 1
            cost -= d * plan[n]
        elif choice == 'm':
            cost += m
            n += 1
            dfs(f_choices, n, cost)
            n -= 1
            cost -= m
        elif choice == 'tm':
            cost += tm
            n += 3
            dfs(f_choices, n, cost)
            n -= 3
            cost -= tm
        elif choice == 'y':
            cost += y
            n += 12
            dfs(f_choices, n, cost)
            n -= 12
            cost -= y


for tc in range(1, T+1):
    # 1일, 1달, 3달, 1년
    d, m, tm, y = map(int, input().split())
    plan = list(map(int, input().split()))
    f_choices = ['d', 'm', 'tm', 'y']
    cost = 0
    n = 0
    result = []
    min_cost = 9999
    dfs(f_choices, n, cost)

    print('#{} {}'.format(tc, min(result)))