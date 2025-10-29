N = int(input())

# Please write your code here.
def f(n):
    if n <= 2:
        return n
    return f(n//3) + f(n-1)

print(f(N))