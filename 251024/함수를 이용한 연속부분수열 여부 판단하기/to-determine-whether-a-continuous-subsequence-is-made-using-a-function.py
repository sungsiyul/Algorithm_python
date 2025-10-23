# n1, n2 = map(int, input().split())
# a = list(map(str, input().split()))
# b = list(map(str, input().split()))

# # Please write your code here.
# print("Yes" if "".join(b) in "".join(a) else "No")

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def f(n1, n2, a, b):
    for i in range(0, n1-n2+1):
        if b == a[i:i+n2]:
            return "Yes"
    return "No"

print(f(n1, n2, a, b))
