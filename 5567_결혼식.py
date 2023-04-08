from collections import deque
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if visited[g] == 0:
                visited[g] = visited[v] + 1
                queue.append(g)


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)
visited[1] = 1
bfs(1)
res = sum([1 for t in visited if 2 <= t <= 3])
print(res)