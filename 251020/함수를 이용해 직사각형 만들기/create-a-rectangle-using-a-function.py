n, m = map(int, input().split())

# Please write your code here.
def f(n, m):
    temp = ''
    for _ in range(m):
        temp += '1'
    for _ in range(n):
        print(temp)
            
f(n, m)