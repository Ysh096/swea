import sys
sys.stdin = open('input.txt', 'r')

#양 옆에 길이 있는지 찾는 함수
def left_or_right(ladder, r, c, pre_c):
    if r == 99:
        return 'stop'
    else:
        if c-1 >= 0 and c+1 <= 99: #에러가 나지 않는 범위에서
            if ladder[r][c-1] == 1 and c-1 != pre_c:
                return 'left'
            else:
                if ladder[r][c+1] == 1 and c+1 != pre_c:
                    return 'right'
                else:
                    return 'down'
        elif c-1 < 0: #왼쪽에 아무것도 없는 경우
            if ladder[r][c+1] == 1 and c+1 != pre_c:
                return 'right'
            else:
                return 'down'
        elif c+1 > 99: #오른쪽에 아무것도 없는 경우
            if ladder[r][c-1] == 1 and c-1 != pre_c:
                return 'left'
            else:
                return 'down'


#10개의 테스트 케이스
for _ in range(1, 11):
    tc = int(input())
    ladder = []
    for _ in range(100):
        ladder += [list(map(int, input().split()))]

    c = 0
    startcol = [] #시작 지점은 [0, startcol의 원소]
    while True:
        try:
            if ladder[0][c] == 0:
                c += 1
            elif ladder[0][c] == 1:
                startcol += [c]
                c += 1
        except:
            break

    for c in startcol: #시작하는 column
        r = 0 #초기 행
        pre_c = c
        ans_c = c
        while True:
            #일단 아래로 항상 내려감
            direction = left_or_right(ladder, r, c, pre_c)
            if direction == 'right':
                pre_c = c
                c += 1
            elif direction == 'left':
                pre_c = c
                c -= 1
            elif direction == 'down':
                r += 1
                pre_c = -1 #down 후에는 pre_c가 필요 없음
            elif direction == 'stop':
                break
        if ladder[r][c] == 2:
            break
        else:
            continue

    print('#{} {}'.format(tc, ans_c))


