import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    # N: 동시에 구울 수 있는 피자의 수
    # M: 구울 피자의 수
    N, M = map(int, input().split())
    # C_list: M개의 피자에 순서대로 올려진 치즈의 양
    C_list = list(map(int, input().split()))
    C_idx = [i for i in range(1, M+1)]
    # 초기화
    que = [] # 화덕
    que_idx = []
    for _ in range(N):
        que.append(C_list.pop(0)) # 처음에 그냥 피자를 다 넣어줘도 된다.
        que_idx.append(C_idx.pop(0))
    while len(que) > 1:
        cheese = que.pop(0) // 2
        idx = que_idx.pop(0)
        if cheese != 0: # 다 녹지 않았을 경우
            que.append(cheese)
            que_idx.append(idx)
        else: # 다 녹았을 경우
            if len(C_list) > 0:
                que.append(C_list.pop(0))
                que_idx.append(C_idx.pop(0))

    print('#{} {}'.format(tc, *que_idx))

# T = int(input())
#
# for test_case in range(T):
#     N, M = map(int, input().split())
#     pizza_cheese = list(map(int, input().split()))
#     pizza = []
#     # 피자의 번호와 치즈양을 함께 사용
#     for i, v in enumerate(pizza_cheese):
#         pizza.append([i + 1, v])
#     # 피자 오븐의 크기만큼 피자를 넣는다
#     pizza_oven = pizza[0:N]
#
#     turn = 0
#     next_pizza = 0
#     count = 0
#     empty = 0
#     while pizza_oven:
#         # 피자 오븐에 피자가 있으면 피자를 돌린다
#
#         # 오븐에서 한 바퀴 돌면 치즈가 녹는다
#         if turn == N and pizza_oven != []: # turn이 N을 고정되려면 오븐의 크기도 고정되어야함
#             for index_one in range(len(pizza_oven)):
#                 pizza_oven[index_one][1] //= 2
#             turn = 0
#
#         # 첫번째 피자의 치즈가 녹으면 꺼내고 새로운 피자를 넣는다
#         if pizza_oven[0][1] == 0 and pizza_oven[0][0] != 0: # [0, 0]을 넣어줘서 생긴 추가조건
#             pizza_oven.pop(0)
#             count += 1
#             if N + next_pizza < M:
#                 pizza_oven = [pizza[N+next_pizza]] + pizza_oven
#                 next_pizza += 1
#             else: # 더 넣을 피자가 없으면
#                 pizza_oven = [[0, 0]] + pizza_oven # 빈 피자판을 추가해줘야함
#                 empty += 1
#
#         # 남은 피자가 없으면 마지막 피자의 번호를 저장
#         if empty == N-1:
#             break
#         # 피자 돌리기
#         tmp = pizza_oven.pop(0)
#         pizza_oven.append(tmp)
#         turn += 1
#     for val in pizza_oven:
#         if val[0] != 0:
#             result = val[0]
#             break
#     print('#{} {}'.format(test_case + 1, result))
