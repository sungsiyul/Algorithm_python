n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for end_idx in range(0, n, 2):
    sorted_target_arr = sorted(arr[:end_idx+1])
    print(sorted_target_arr[end_idx//2], end=' ')

