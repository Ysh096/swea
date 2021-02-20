import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for idx in range(1, T+1):
    L = int(input())
    card_list = list(input())
    card_dict = {}
    for i in card_list:
        try:
            card_dict[i] += 1 #같은 숫자가 있을 경우 +1
        except:
            card_dict[i] = 1 #같은 숫자가 없을 경우 1을 원소로
    max_value = 0
    max_key = 0
    for key, value in card_dict.items():
        if value > max_value:
            max_value = value #가장 많은 카드 개수
            max_key = int(key) #가장 많은 카드의 number
        elif value == max_value: #카드 수가 겹치는 경우
            if max_key < int(key):
                max_key = int(key) #가장 큰 수를 가진 카드 number
    print('#{} {} {}'.format(idx, max_key, max_value))

