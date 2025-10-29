N = int(input())

# Please write your code here.

def f(i):
    if i <= 2:
        return i*2
    return (f(i-2)*f(i-1))%100

print(f(N))
