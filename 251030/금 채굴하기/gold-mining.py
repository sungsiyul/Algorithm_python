n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def count_gold_in_range(start_x, start_y, k, grid, n):
    """맨해튼 거리가 k 이하인 영역의 금 개수를 세기"""
    count = 0
    for i in range(n):
        for j in range(n):
            if abs(i - start_x) + abs(j - start_y) <= k:
                if grid[i][j] == 1:
                    count += 1
    return count

# 전체 금의 개수를 미리 계산
total_gold = sum(sum(row) for row in grid)

max_num_of_gold = 0

# k의 상한: 비용이 전체 금 가치를 초과하면 의미 없음
max_k = n + 1
for k in range(max_k):
    cost = k * k + (k + 1) * (k + 1)
    
    # 전체 금을 다 캐도 손해면 더 큰 k는 볼 필요 없음
    if cost > total_gold * m:
        break
    
    for x in range(n):
        for y in range(n):
            num_of_gold = count_gold_in_range(x, y, k, grid, n)
            if num_of_gold * m >= cost:
                max_num_of_gold = max(max_num_of_gold, num_of_gold)

print(max_num_of_gold)