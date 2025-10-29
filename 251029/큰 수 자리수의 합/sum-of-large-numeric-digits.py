a, b, c = map(int, input().split())

# Please write your code here.
def f(v):
    if v < 10:
        return v
    return v%10 + f(v//10)

print(f(a*b*c))