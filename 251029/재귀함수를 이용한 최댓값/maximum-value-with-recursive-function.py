n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def max_value(a):
    if a == 0:
        return arr[0]
    return max(arr[a], max_value(a-1))

print(max_value(n-1))