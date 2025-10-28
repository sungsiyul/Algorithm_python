N = int(input())

# Please write your code here.
def f(N):
    if N == 1:
        return 1
    return N + f(N-1)

print(f(N))