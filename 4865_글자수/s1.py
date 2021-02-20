import sys
sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
# 	#문자를 어떻게 리스트의 원소로 나눠서 받을지 좀 헷갈려서 map을 쓰려고 합니다.
# 	#쓰는김에 ord를 써주면 생각하기 편할 것 같아서 썼습니다.
#     str1 = set(list(map(ord, input()))) #겹치는 문자 제거
#     str2 = list(map(ord, input()))
#
#     pre_cnt = 0
#     cnt = 0
#     for val_1 in str1:
#         for val_2 in str2:
#             if val_1 == val_2: #단순 값 비교
#                 pre_cnt += 1 #같으면 그만큼 카운트를 늘려주고
#         if pre_cnt > cnt: #카운트의 최댓값을 cnt에 저장합니다.
#             cnt = pre_cnt
#             pre_cnt = 0
#         else:
#             pre_cnt = 0
#     print('#{} {}'.format(tc, cnt))

####재현님 풀이####
import sys
sys.stdin = open('input.txt')
test = int(input())

for t in range(1, test + 1):
    s1 = set(input())
    s2 = input()
    dict1 = dict() # 딕셔너리

    for ele1 in s1:
        dict1[ele1] = s2.count(ele1)

    max_value = 0 # 딕셔너리 중 max 값 저장하여 출력
    for value in dict1.values():
        max_value = max(max_value, value)

    print('#{} {}'.format(t, max_value))
