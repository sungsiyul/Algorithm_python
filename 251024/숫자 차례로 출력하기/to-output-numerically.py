n = int(input())

# Please write your code here.
def f(N):
    if N == 0:
        return
    f(N-1)
    print(N, end=" ")

def g(N):
    if N == 0:
        return
    print(N, end=" ")
    g(N-1)    

f(n)
print()
g(n)
