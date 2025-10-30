n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def is_in_a_grid(x, y, n):
    return x >= 0 and x <= n-1 and y >= 0 and y <= n-1

def bfs(start_x, start_y, k, grid):
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    num_of_gold = 0

    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True
    if grid[start_x][start_y] == 1:
        num_of_gold += 1
        
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]
    
    while queue:
        cur_x, cur_y, cur_step = queue.popleft()
        next_step = cur_step + 1
        if next_step <= k:
            for dx, dy in zip(dxs, dys):
                next_x, next_y = cur_x + dx, cur_y + dy
                if is_in_a_grid(next_x, next_y, n):
                    if visited[next_x][next_y] == False:
                        # 갈 수 있는 곳이라면 일단 가기
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y, next_step))
                        # 그 중 gold가 있으면 counting
                        if grid[next_x][next_y] == 1:                            
                            num_of_gold += 1
    return num_of_gold
    
num_of_gold_list = []
for k in range(n):
    for y in range(n):
        for x in range(n):
            num_of_gold = bfs(x, y, k, grid)
            if num_of_gold * m >= k**2 + (k+1)**2:
                num_of_gold_list.append(num_of_gold)

print(max(num_of_gold_list))