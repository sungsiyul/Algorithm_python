n1, n2 = map(int, input().split())
a = list(map(str, input().split()))
b = list(map(str, input().split()))

# Please write your code here.

print("Yes" if "".join(b) in "".join(a) else "No")