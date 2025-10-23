n = int(input())

# Please write your code here.
def f(n):
    l = [i for i in range(1, n+1)]
    return int(sum(l) / 10)

print(f(n))