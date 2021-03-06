import sys
sys.stdin = open("input.txt", "r")
# 1은 가위, 2는 바위, 3은 보
# 같은 카드인 경우 번호가 작은 쪽이 승자
def rsp(N, cards, idx):
    if len(cards) == 1: # 한 명 남은 경우
        return [cards[0], idx[0]]
    if len(cards) == 2: # 두 명만 남은 경우
        if cards[0] == cards[1]: # 같은 경우
            return [cards[0], idx[0]]
        elif cards[0] == 1 and cards[1] == 2:
            return [cards[1], idx[1]]
        elif cards[0] == 1 and cards[1] == 3:
            return [cards[0], idx[0]]
        elif cards[0] == 2 and cards[1] == 1:
            return [cards[0], idx[0]]
        elif cards[0] == 2 and cards[1] == 3:
            return [cards[1], idx[1]]
        elif cards[0] == 3 and cards[1] == 1:
            return [cards[1], idx[1]]
        elif cards[0] == 3 and cards[1] == 2:
            return [cards[0], idx[0]]
    else:
        if N % 2:
            N = N // 2 + 1
        else:
            N = N // 2
        # 주의: 갈라진 후에는 N이 달라짐
        A = rsp(len(cards[:N]), cards[:N], idx[:N]) # A의 첫 번째 원소: 카드번호, 두 번째 원소: 몇 번째 사람인지
        B = rsp(len(cards[N:]), cards[N:], idx[N:]) # B의 첫 번째 원소: 카드번호, 두 번째 원소: 몇 번째 사람인지
    if A[0] == B[0]:
        return A
    elif A[0] == 1 and B[0] == 2:
        return B
    elif A[0] == 1 and B[0] == 3:
        return A
    elif A[0] == 2 and B[0] == 1:
        return A
    elif A[0] == 2 and B[0] == 3:
        return B
    elif A[0] == 3 and B[0] == 1:
        return B
    elif A[0] == 3 and B[0] == 2:
        return A

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    idx = [i for i in range(1, len(cards)+1)]
    print('#{} {}'.format(tc, rsp(N, cards, idx)[1]))