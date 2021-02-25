# 어떤 사람의 경로에 출발지나 목적지가 속해 있는 경우, 단위시간 +1
# 앞의 모두와 비교해야 함. (한명이라도 겹치면 그냥 +1 하고 끝!)
import sys
sys.stdin = open('input.txt')
T = int(input())
def changenum(i: int)->int:
    if i % 2:
        return i//2 + 1
    else:
        return i//2
for tc in range(1, T+1):
    rooms = [0]*201
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        a = changenum(a)
        b = changenum(b)
        for i in range(a, b+1):
            rooms[i] += 1
    print('#{} {}'.format(tc, max(rooms)))