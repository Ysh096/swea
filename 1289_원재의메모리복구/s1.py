#초기화 상태(모든 bit가 0)에서 원래 상태로 돌아가는데
#최소 몇 번이나 고쳐야 하는가?
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    goal = list(map(int, input()))
    present = [0]*len(goal)
    #가장 앞에 있는애부터 바꿔가야함
    cnt = 0
    end = len(goal)
    for i in range(end):
        if goal[i] == present[i]:
            continue
        else:
            for j in range(i, end):
                present[j] = goal[i]
            cnt+= 1
    print('#{} {}'.format(tc, cnt))