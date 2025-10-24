n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 해당 수열이 동일 원소가 M개 이상 연속으로 나오는가?
def is_happy_arr(arr, m):
    max_cnt, cnt = 1, 1
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            cnt += 1
        else:
            cnt = 1
        # if cnt >= m:
        #     return 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt >= m

# def is_happy_arr(arr, m):
#     cons_cnt, max_cnt = 1, 1
#     for i in range(len(arr)):
#         if arr[i-1] == 

# 각 행마다
fin_cnt = 0
cols = []
for row in grid:
    fin_cnt += is_happy_arr(row, m)
# 행렬전환
_grid = list(zip(*grid))
# # 각 열마다
for col in _grid:
    fin_cnt += is_happy_arr(col, m)

# col = [0] * n
# for j in range(n):
#     for i in range(n):
#         col[i] = grid[i][j]
#     fin_cnt += is_happy_arr(col, m)

print(fin_cnt)


