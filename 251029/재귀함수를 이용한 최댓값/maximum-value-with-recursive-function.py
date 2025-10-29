n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

max_v = 1
for a in arr:
    max_v = max(max_v, a)
print(max_v)
