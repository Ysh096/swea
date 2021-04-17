import sys
sys.stdin = open('input.txt')
def go(x, y, cnt, num):
    if cnt == 6:
        answer_set.add(int(num))
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue
        go(nx, ny, cnt+1, num+arr[nx][ny])


T = int(input())

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    answer_set = set()
    for i in range(4):
        for j in range(4):
            go(i, j, 0, arr[i][j])

    print('#{} {}'.format(tc, len(answer_set)))