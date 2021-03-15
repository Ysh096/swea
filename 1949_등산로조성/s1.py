import sys
sys.stdin = open("input.txt")

# def dfs(pos, visited, cnt, max_len):
#     '''
#     pos: positions [i, j], 처음엔 최대 높이의 위치들이 담겨있음.
#     visited: 방문 표시를 위한 이차원 리스트
#     '''
#     while pos:
#         r, c = pos.pop(-1)
#         visited[r][c] = 1
#         for k in range(4):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < N and 0 <= nc < N:
#                 if roads[r][c] > roads[nr][nc] and visited[nr][nc] == 0:
#                     pos.append([nr, nc])
#                     cnt += 1
#                     dfs(pos, visited, cnt, max_len)
#                     visited[nr][nc] = 0
#                     cnt -= 1
#         # for 문이 끝나면 갈 곳이 없다는 뜻
#         max_len.append(cnt)
#
# T = int(input())
# # 지도의 한 변의 길이 N
# # 최대 공사 가능 깊이 K
# N, K = map(int, input().split())
#
# dr = [-1, 1, 0, 0] # 상하좌우
# dc = [0, 0, -1, 1]
# for tc in range(1, T+1):
#     max_len = []
#     roads = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0]*N for _ in range(N)]
#     positions = [] # 가장 높은 위치들
#     max_val = max(max(roads))
#     for i in range(N):
#         for j in range(N):
#             if roads[i][j] == max_val:
#                 positions.append([i, j])
#     cnt = 0
#
#     dfs(positions, visited, cnt, max_len)
'''
point
1. dfs 이지만 갔던 경로는 방문 해제를 풀어서 모든 경로를 탐색해야 한다.
2. 깎은 곳은 깎은 상태로 저장했다가 되돌아가면서 원래값으로 돌려놔야 한다.
3. 더 이상 갈 곳이 없으면 그 경로는 종료된다. 이 때 최대 거리라면 갱신해주어야한다.
4. 어디 갔다가 돌아와서 함수가 종료된 것인지, 찐 종료된 것인지 구분해주었다 근데 구분안해도 똑같은거같다..
5. 다른 효과적인 풀이가 있나 찾아봐야겠다
'''
def dfs(x, y, status, cnt, K, visited):
    global max_distance
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True

    end = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if visited[nx][ny]:
            continue
        if my_map[x][y] <= my_map[nx][ny] < my_map[x][y] + K and status == 0:
            t = my_map[nx][ny]
            my_map[nx][ny] = my_map[x][y] - 1
            dfs(nx, ny, 1, cnt + 1, K, visited)
            my_map[nx][ny] = t # 깎은거 원래대로 돌려놓기
            end = False
        elif my_map[nx][ny] < my_map[x][y]:
            dfs(nx, ny, status, cnt + 1, K, visited)
            end= False

    visited[x][y] = False
    if end and max_distance < cnt:
        max_distance = cnt


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    # 최대값 찾기
    max_value = 0
    for i in range(N):
        for j in range(N):
            if my_map[i][j] > max_value:
                max_value = my_map[i][j]
    # 최대값인 인덱스 모두 기록
    starts = []
    for i in range(N):
        for j in range(N):
            if my_map[i][j] == max_value:
                starts.append((i, j))
    # 모든 시작점에서의 최대 거리
    ans = 0
    for r, c in starts:
        visited = [[False for _ in range(N)] for _ in range(N)]
        # 현재 시작점에서의 최대 거리
        max_distance = 1
        # (행, 열, 산을 깎았는 지 여부, 이동거리, 최대공사가능깊이)
        dfs(r, c, 0, 1, K, visited)
        if ans < max_distance:
            ans = max_distance
    print('#{} {}'.format(tc, ans))