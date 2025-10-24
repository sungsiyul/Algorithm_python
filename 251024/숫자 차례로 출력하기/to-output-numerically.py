n = int(input())

# Please write your code here.
def g(N):
    if N == 0:
        return
    print(N, end=" ")
    g(N-1)    

a = [str(i+1) for i in range(n)]
a = " ".join(a)
print(a)
g(n)
