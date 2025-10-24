n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
# 최대 이동 범위 전체 크기 - 작은 grid 크기
max_cnt = 0
for i in range(len(grid)-3+1):
    for j in range(len(grid)-3+1):
        cnt = sum([sum(row[j:j+3]) for row in grid[i:i+3]])
        if cnt > max_cnt:
            max_cnt = cnt
print(max_cnt)
    