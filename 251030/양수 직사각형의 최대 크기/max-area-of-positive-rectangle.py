n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def get_area_size(row, col, height, width):
    area_size = 0
    for h in range(height):
        for w in range(width):
            v = grid[row + h][col + w]
            if v < 0:
                return -1
            area_size += 1
    return area_size

max_area_size = -1
# 시작점
for row in range(n):
    for col in range(m):
        # 너비 및 높이
        for height in range(1, (n-row)+1):
            for width in range(1, (m-col)+1):
                # area: 각 포인트로부터 정해진 height, width 내 point 집합
                area_size = get_area_size(row, col, height, width)
                max_area_size = max(max_area_size, area_size)
print(max_area_size)