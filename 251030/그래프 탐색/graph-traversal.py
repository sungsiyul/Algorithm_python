n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import defaultdict
graph = defaultdict(list)

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# print(graph)

visited = set()

cnt = 0
def dfs(cur_v):
    global cnt
    visited.add(cur_v)
    for next_v in graph[cur_v]:
        if next_v not in visited:
            cnt += 1
            dfs(next_v)

dfs(1)
print(cnt)