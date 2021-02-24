import sys
sys.stdin = open('input.txt')

#S, D, H, C 순서로 몇 장의 카드가 부족한지 출력하라.
#겹치는 카드가 있을 경우 오류발생
T = int(input())
def card_check(cards):
    card_dict = {'S': [], 'D': [], 'H': [], 'C': []}
    for i in range(len(cards)):
        if i % 3 == 0:
            tmp_key = cards[i]
        elif i % 3 == 1:
            tmp_val = cards[i]
        elif i % 3 == 2:
            tmp_val += cards[i]
            card_dict[tmp_key].append(tmp_val)
    #card_dict에 데이터가 저장된 형태는
    #{'S': ['01'], 'H': ['03', '04'], 'D': ['02'], 'C': []}
    for value in card_dict.values():
        if len(set(value)) != len(value):
            return ['ERROR']
    #ERROR가 나지 않으면 다음의 동작을 수행한다.
    order = ['S', 'D', 'H', 'C']
    result = []
    for i in range(4):
        result.append(13 - len(card_dict[order[i]]))
    return result

for tc in range(1, T+1):
    cards = input()
    print('#{}'.format(tc), *card_check(cards))