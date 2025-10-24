n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

def bfs(maps):
    rows = len(maps)
    cols = len(maps[0])

    queue = deque()
    queue.append((0, 0))
    
    visited = [[False] * cols for _ in range(rows)]

    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == rows - 1 and cur_y == cols - 1:
            return 1
        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x + dx, cur_y + dy
            if next_x >= 0 and next_x <= rows-1 and next_y >= 0 and next_y <= cols-1:
                if maps[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
    return 0

print(bfs(a))
    
