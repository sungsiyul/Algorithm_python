n = int(input())

# Please write your code here.
def f(N):
    if N == 1:
        return 0
    if N % 2 == 0:
        return 1 + f(N//2)
    else:
        return 1 + f(N*3+1)

print(f(n))