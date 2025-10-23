a, b = map(int, input().split())

# Please write your code here.

def check(n):
    if n == 2 or n == 3:
        return True
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

acc = 0
for i in range(a, b+1):
    if check(i): acc += i
print(acc)