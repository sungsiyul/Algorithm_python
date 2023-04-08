N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]    #0~7까지, 7은 버리는 index

for i in range(N-1, -1, -1):
    if i + grid[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], grid[i][1]+dp[i+grid[i][0]])

print(dp[0])