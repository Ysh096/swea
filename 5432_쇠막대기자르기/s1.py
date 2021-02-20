import sys
sys.stdin = open('input.txt')

#인접한 것은 무조건 레이저라고 하고, 떨어진 것은 쇠막대기라고 하자.
#괄호를 모두 리스트로 받아와서 우선 인접한 괄호의 수를 세자.
# T = int(input())
# for tc in range(1, T+1):
#     probs = list(input())
#
#     i = 0
#     iron = 0
#     piece = 0
#     while i < len(probs):
#         if probs[i] == '(':
#             if probs[i+1] == ')': #바로 닫히면(레이저면)
#                 if iron != 0: #자를 iron이 있을 때 잘린 iron의 수를 구한다.
#                     piece += iron #자른 조각의 수
#                     i += 2 #레이저 다음으로 넘어간다.
#                 else:
#                     i += 1 #자를게 없으면 다음 순서로
#             else: #바로 닫히지 않으면 <- '(' 이 오면
#                 iron += 1 #iron이 하나 늘어난 것과 마찬가지
#                 i += 1
#         else: # 레이저가 아닌데 ')'가 오면 iron이 끝났다는 뜻.
#             i += 1
#             if not iron == 0: #역시 iron이 0이 아닐 때만(레이저가 자를 게 있을때만)
#                 piece += 1
#                 iron -= 1
#     print('#{} {}'.format(tc, piece))

T = int(input())
for tc in range(1, T+1):
    probs = list(input())
    i = 0
    iron = 0
    piece = 0
    while i < len(probs):
        if probs[i] == '(':
            if probs[i+1] == ')': #바로 닫히면(레이저면)
                if iron > 0: #자를 iron이 있을 때 잘린 iron의 수를 구한다.
                    piece += iron #자른 조각의 수
                    i += 2 #레이저 다음으로 넘어간다.
                else:
                    i += 1
            else: #바로 닫히지 않으면 <- '(' 이 오면
                iron += 1 #iron이 하나 늘어난 것과 마찬가지
                i += 1
        else: # 레이저가 아닌데 ')'가 오면 iron이 끝났다는 뜻.
            i += 1
            if iron != 0: #역시 iron이 0이 아닐 때만(레이저가 자를 게 있을때만)
                piece += 1
                iron -= 1

    print('#{} {}'.format(tc, piece))
