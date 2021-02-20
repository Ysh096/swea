import sys
sys.stdin = open("input.txt", "r")

T = int(input())
#목적지를 찾아가는 함수
def solution(P, destination):
    l = 1 #start
    r = P #end
    cnt = 0
    while True:
        m = int((l+r)/2)
        if m == destination:
            # cnt += 1 넣을 필요 없음. 비교가 목적이므로
            return cnt
        elif m > destination:
            r = m
        else:
            l = m
        cnt += 1

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    a, b = solution(P, Pa), solution(P, Pb)
    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))


####재귀(석환님)
# import sys
# sys.stdin = open("input.txt", 'r')
# ​
# def binary_recursion(start, end, goal):
#     mid = int((start+end)/2)
#     if mid == goal:
#         return 1
#     elif mid > goal:
#         return binary_recursion(start, mid, goal) + 1 #카운트를 위한 것
#     else:
#         return binary_recursion(mid, end, goal) + 1
# ​
# ​
# ​
# ​
# for tc in range(1, int(input())+1):
#     P, A, B = map(int, input().split())
#     count_a = binary_recursion(1, P, A) #책을 펼친 횟수
#     count_b = binary_recursion(1, P, B)
# ​
#     if count_a < count_b:
#         ans = 'A'
#     elif count_a > count_b:
#         ans = 'B'
#     else:
#         ans = 0
#     print("#{} {}".format(tc, ans))