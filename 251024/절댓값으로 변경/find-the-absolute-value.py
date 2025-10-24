n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def abs(i):
    if i < 0:
        return -i
    else:
        return i

for a in arr:
    print(abs(a), end=" ")
