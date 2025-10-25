n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

# n 격자 크기
# k 시작점의 수
# grid
# points: 시작점 위치

from collections import deque

def bfs(start_points, maps):
    rows = len(maps)
    cols = len(maps[0])
    queue = deque()
    visited = [[False] * cols for _ in range(rows)]
    for start_x, start_y in start_points:
        queue.append((start_x-1, start_y-1))
        visited[start_x-1][start_y-1] = True
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]
    while queue:
        cur_x, cur_y = queue.popleft() 
        for dx, dy in zip(dxs, dys):
            next_x = cur_x + dx
            next_y = cur_y + dy
            if next_x >= 0 and next_x <= rows-1 and next_y >= 0 and next_y <= cols-1:
                if maps[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
                    
    return visited

visited = bfs(points, grid)
cnt = 0
for v_row in visited:
    for v in v_row:
        if v: cnt += 1
print(cnt)