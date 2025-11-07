n = int(input())
nums = list(map(int, input().split()))

nums.sort()

max_v = 0
for i in range(n):
    v = nums[i] + nums[2*n-i-1]
    max_v = max(max_v, v)
print(max_v)