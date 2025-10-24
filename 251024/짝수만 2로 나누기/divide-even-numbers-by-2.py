n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def divide_even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
    return arr

for a in divide_even(arr):
    print(a, end=" ")