a, b = map(int, input().split())

# Please write your code here.

def check(n):
    if n % 2 == 0 or n % 10 == 5 or (n % 3 == 0 and n % 9 != 0):
        return False
    return True

cnt = 0
for i in range(a, b+1):
    if check(i): cnt += 1
print(cnt)