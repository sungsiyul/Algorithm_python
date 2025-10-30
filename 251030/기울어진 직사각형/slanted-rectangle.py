n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 방향 이동 (1, -1), (-1, -1) (-1, 1) (1, 1)
# 1번 방향 이동 횟수 == 3번 방향 이동 횟수
# 2번 방향 이동 횟수 == 4번 방향 이동 횟수

moving_arrow = [(0, 0), (1, -1), (-1, -1), (-1, 1), (1, 1)]

def get_area_sum(x, y, odd_arrow, even_arrow):
    area_sum = 0
    for i in range(1, 5):
        num_arrow = even_arrow if i % 2 == 0 else odd_arrow
        for _ in range(num_arrow):
            x, y = x + moving_arrow[i][0], y + moving_arrow[i][1]
            if 0 <= x < n and 0 <= y < n:
                area_sum += grid[x][y]
            else:
                return 0
    return area_sum


max_area_sum = 0
for odd_arrow in range(1, n):
    for even_arrow in range(1, n):
        for y in range(n):
            for x in range(n):
                max_area_sum = max(max_area_sum, get_area_sum(x, y, odd_arrow, even_arrow))
print(max_area_sum)