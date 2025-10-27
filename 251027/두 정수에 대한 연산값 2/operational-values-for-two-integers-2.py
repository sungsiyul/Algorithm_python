a, b = map(int, input().split())

# Please write your code here.
def f(a, b):
    if a < b:
        a = a + 10
        b = b * 2
    else:
        b = b + 10
        a = a * 2
    return a, b
a, b = f(a, b)
print(a, b)