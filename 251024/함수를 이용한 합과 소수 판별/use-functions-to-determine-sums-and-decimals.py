a, b = map(int, input().split())

# Please write your code here.
def check_prime(n):
    if n <= 3: return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_sum_even(n):
    return ((n % 10) + (n // 10)) % 2 == 0

cnt = 0
for i in range(a, b+1):
    if check_prime(i) and check_sum_even(i):
        cnt += 1
print(cnt)
