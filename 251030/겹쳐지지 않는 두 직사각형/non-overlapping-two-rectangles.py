n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 1) 가능한 직사각형 (정사각형 포함) 만들기
def get_candidates(n, m, grid):
    candi = []
    for row in range(n):
        for col in range(m):
            for row_len in range(1, n - row + 1):
                for col_len in range(1, m - col + 1):
                    v_sum = 0
                    points = []
                    for r in range(row, row + row_len):
                        for c in range(col, col + col_len):
                            v_sum += grid[r][c]
                            points.append((r, c))
                    candi.append([points, v_sum])
    return candi

def is_overlap(std_points, comp_points):
    for comp_p in comp_points:
        if comp_p in std_points:
            return True
    return False

# 2) 그 중 겹치지 않는 2개의 직사각형 뽑은 뒤 합 -> max
def get_max_value(pool):
    max_v = -1000
    # 기준이 되는 박스
    for i in range(len(pool)):
        std_v = pool[i]
        # 비교 대상 박스 1개씩
        for j in range(len(pool)):
            if i != j:
                comp_v = pool[j]
                # 직사각형을 이루고 있는 좌표가 1개라도 겹친다면, -> 다음 비교 박스로
                if not is_overlap(set(std_v[0]), set(comp_v[0])):
                    two_sum = std_v[1] + comp_v[1]
                    max_v = max(max_v, two_sum)
    return max_v


pool = get_candidates(n, m, grid)
max_v = get_max_value(pool)
print(max_v)