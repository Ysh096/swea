import sys
sys.stdin = open("input.txt")

# 딱 한 번 K 깊이만큼 지형을 깎을 수 있다.
# 깎을 때 다 깎아볼 필요는 없고 현재 위치에서 이동 가능한 정도로만 깎으면 된다.
# 9 -> 8이 되도록 깎기, 6 -> 5가 되도록 깎기

# A형은 완전탐색을 하되 중복을 제거해주면 된다.
# 1을 0으로 깎는 것도 가능하다.

# 경로가 가장 길어질 수 있는 어떤 부분을 내가 골라서 깎는다고 생각할 수는 없고,
# 그냥 길이 막히면 깎아야 한다. 일단 깎아서 더 가야 그 다음이 있는거니까
# 두 번 깎을 수 없다! 가 매우 중요한 포인트
def dfs(i, j, c, cnt, visited):
    '''
    i, j: 진입한 칸의 좌표
    c: 남은 깎음 횟수
    s: 이전까지의 등산로 길이
    '''
    # 방문 표시
    visited[i][j] = 1
    # 다음 위치를 보고 갈 수 있으면 가본다.
    for k in range(4):
        # 새로 확인할 위치
        nr = i + dr[k]
        nc = j + dc[k]
        # 1-1) 새로운 경로가 지도 내에 위치하고 방문하지 않았다면
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] != 1:
            # 2-1) 현재 높이보다 낮은지 확인
            if jido[nr][nc] < jido[i][j]: # 낮으면
                visited[i][j] = 1 # 방문
                cnt += 1 # 길이 +1
                dfs(nr, nc, c, cnt, visited) # 다음 경로로
                cnt -= 1 # 다음 경로 확인이 끝나면 원상복구
            else: # 2-2) 현재 높이보다 낮지 않으면
                #  3-1) 최대 깊이인 K만큼 깎아서 현재 높이보다 낮아질 수 있으면
                if jido[nr][nc] - K < jido[i][j] and c == 1:
                    pre_val = jido[nr][nc]
                    jido[nr][nc] = jido[i][j] - 1 # 그렇게 만들어 주고
                    c = 0 # 깎음 횟수 0
                    visited[nr][nc] = 1 # 방문표시
                    cnt += 1 # 길이 + 1
                    dfs(nr, nc, c, cnt, visited) # 다음 경로로
                    jido[nr][nc] = pre_val # 다음 경로 확인이 끝나면 원상복구
                    c = 1
                    cnt -= 1
                else: # 3-2) 깎아도 더 갈 수 없으면 다음 경로 확인
                    continue

        else: # 1-2) 새로운 경로가 지도 내에 없으면 다음 위치 확인
            continue
    # 4) for문이 끝났으면
    result.append(cnt)
    visited[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    # 한 변의 길이 N, 최대 공사 가능 깊이 K
    N, K = map(int, input().split())
    # N*N 지도 정보
    jido = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_val = 0
    # 최댓값 찾기
    for row in jido:
        if max(row) > max_val:
            max_val = max(row)
    # 최댓값 위치 찾기
    max_hs = []
    for i in range(N):
        for j in range(N):
            if jido[i][j] == max_val:
                max_hs.append((i, j))

    dr = [-1, 1, 0, 0] # 상하좌우
    dc = [0, 0, -1, 1]
    result = []
    while max_hs:
        # 남은 깎음 횟수
        c = 1
        cnt = 1
        i, j = max_hs.pop()
        dfs(i, j, c, cnt, visited)
    print('#{} {}'.format(tc, max(result)))