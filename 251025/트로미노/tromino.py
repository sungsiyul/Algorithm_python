n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def rotate_blocks_1(i, j, n, m, grid):
    max_sum = 0
    ratations = [[i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j+1]]
    for ratation in ratations:
        if ratation[0] <= n-1 and ratation[0] >= 0 and ratation[1] <= m-1 and ratation[1] >= 0:
            block_sum = grid[i][j] + grid[ratation[0]][j] + grid[i][ratation[1]]
            if max_sum < block_sum:
                max_sum = block_sum
    return max_sum

def rotate_blocks_2(i, j, n, m, grid):
    max_sum = 0
    if j+2 <= m-1:
        max_sum = max(max_sum, grid[i][j] + grid[i][j+1] + grid[i][j+2])
    if i+2 <= n-1:
        max_sum = max(max_sum, grid[i][j] + grid[i+1][j] + grid[i+2][j])
    return max_sum

total_max_sum = 0
for i in range(n):
    for j in range(m):
        block_1_max_sum = rotate_blocks_1(i, j, n, m, grid)
        block_2_max_sum = rotate_blocks_2(i, j, n, m, grid)
        total_max_sum = max(total_max_sum, block_1_max_sum, block_2_max_sum)
        
print(total_max_sum)
